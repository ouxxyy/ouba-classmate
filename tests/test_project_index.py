"""Behavior checks for project index generation, with fixed input and no network."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("update_projects",ROOT/"scripts/update_projects.py")
index=importlib.util.module_from_spec(spec)
spec.loader.exec_module(index)

class ProjectIndexTests(unittest.TestCase):
    def repos(self):
        return [
            {"name":"storyboard-scavenger","html_url":"https://github.com/ouxxyy/storyboard-scavenger",
             "description":"Upstream description","language":"HTML","stargazers_count":5,
             "updated_at":"2026-10-20T03:15:54Z","fork":False},
            {"name":"new-example","html_url":"https://github.com/ouxxyy/new-example",
             "description":"A new useful tool","language":None,"stargazers_count":0,
             "updated_at":"2026-10-19T00:00:00Z","fork":False}]
    def test_handwritten_sections_survive_repeated_generation(self):
        before="# Header\n\n手写介绍\n"+index.START_MARK+"\nold\n"+index.END_MARK+"\n\n尾部说明\n"
        first=index.replace_project_block(before,self.repos())
        self.assertEqual(first,index.replace_project_block(first,self.repos()))
        self.assertEqual(first.split(index.START_MARK)[0],before.split(index.START_MARK)[0])
        self.assertEqual(first.split(index.END_MARK)[1],before.split(index.END_MARK)[1])
        self.assertIn(index.REPO_META["storyboard-scavenger"]["desc"],first)
        self.assertIn("更多项目",first)
    def test_catalog_preserves_old_field_values_and_adds_discovery(self):
        catalog=index.build_catalog(self.repos(),"fixed")
        self.assertEqual(catalog,index.build_catalog(self.repos(),"fixed"))
        self.assertEqual(catalog["generated_at"],"fixed")
        for source,out in zip(self.repos(),catalog["projects"]):
            expected={"name":source["name"],"url":source["html_url"],
                      "description":index.REPO_META.get(source["name"],{}).get("desc") or source["description"] or "",
                      "category":index.REPO_META.get(source["name"],{}).get("category","more"),
                      "language":source["language"] or "",
                      "stars":source["stargazers_count"],"updated_at":source["updated_at"]}
            self.assertEqual({k:out[k] for k in expected},expected)
        self.assertTrue(catalog["projects"][0]["description_en"])
        self.assertIn("AI video storyboard",catalog["projects"][0]["keywords"])
        self.assertEqual(catalog["projects"][1]["description_en"],"")
        self.assertEqual(catalog["projects"][1]["keywords"],[])
        self.assertEqual(catalog["projects"][1]["use_cases"],[])
    def test_missing_duplicate_and_reversed_markers_are_rejected(self):
        for value in ["none",index.START_MARK+index.START_MARK+index.END_MARK,index.END_MARK+index.START_MARK]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                index.replace_project_block(value,self.repos())
    def test_new_project_metadata_reaches_both_outputs(self):
        entry={"category":"local","desc":"新项目关键词","description_en":"new tool",
               "keywords":["new tool"],"use_cases":["new task"]}
        with patch.dict(index.REPO_META,{"new-example":entry}):
            self.assertIn("新项目关键词",index.replace_project_block(index.START_MARK+index.END_MARK,self.repos()))
            out=index.build_catalog(self.repos(),"fixed")["projects"][1]
            self.assertEqual(out["description_en"],"new tool")
            self.assertEqual(out["keywords"],["new tool"])
            self.assertEqual(out["use_cases"],["new task"])
    def test_main_does_not_write_on_invalid_readme(self):
        with tempfile.TemporaryDirectory() as tmp:
            readme=Path(tmp)/"README.md"; catalog=Path(tmp)/"projects.json"
            readme.write_text("no markers");catalog.write_text("original catalog")
            with patch.object(index,"README_PATH",str(readme)),patch.object(index,"JSON_PATH",str(catalog)),patch.object(index,"fetch_repos",return_value=self.repos()):
                with self.assertRaises(SystemExit): index.main()
            self.assertEqual(readme.read_text(),"no markers")
            self.assertEqual(catalog.read_text(),"original catalog")
if __name__=="__main__":
    unittest.main()

