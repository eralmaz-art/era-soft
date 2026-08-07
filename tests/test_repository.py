from __future__ import annotations

import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class RepositoryContractTest(unittest.TestCase):
	def test_frappe_packages_exist_for_every_module(self) -> None:
		modules = (ROOT / "era_soft" / "modules.txt").read_text(encoding="utf-8").splitlines()
		for module in filter(None, modules):
			package = module.lower().replace(" ", "_")
			with self.subTest(module=module):
				self.assertTrue((ROOT / "era_soft" / package / "__init__.py").is_file())

	def test_supported_major_versions_are_bounded(self) -> None:
		config = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
		self.assertIn('frappe = ">=16.0.0,<17.0.0"', config)
		self.assertIn('erpnext = ">=16.0.0,<17.0.0"', config)

	def test_no_erpnext_source_is_vendored(self) -> None:
		self.assertFalse((ROOT / "erpnext").exists())

	def test_visual_baseline_contains_no_custom_doctypes(self) -> None:
		doctype_directories = list((ROOT / "era_soft").glob("**/doctype"))
		self.assertEqual(doctype_directories, [])

	def test_navigation_matches_approved_order(self) -> None:
		sidebar_path = ROOT / "era_soft" / "workspace_sidebar" / "construction.json"
		sidebar = json.loads(sidebar_path.read_text(encoding="utf-8"))
		self.assertEqual(
			[item["label"] for item in sidebar["items"]],
			[
				"Dashboard",
				"Construction",
				"Procurement",
				"Finance",
				"Projects",
				"Suppliers",
				"Employees",
				"Reports",
				"Settings",
			],
		)

	def test_visual_configuration_files_are_valid_json(self) -> None:
		configuration_paths = [
			ROOT / "era_soft" / "desktop_icon" / "era_soft.json",
			ROOT / "era_soft" / "workspace_sidebar" / "construction.json",
			*sorted((ROOT / "era_soft").glob("**/workspace/**/*.json")),
		]
		for path in configuration_paths:
			with self.subTest(path=path):
				json.loads(path.read_text(encoding="utf-8"))

	def test_visual_assets_and_launcher_exist(self) -> None:
		for relative_path in (
			"era_soft/public/images/era-soft-mark.svg",
			"era_soft/public/images/era-soft-logo.svg",
			"era_soft/public/css/era_soft.css",
			"macos/ERA SOFT.command",
		):
			with self.subTest(relative_path=relative_path):
				self.assertTrue((ROOT / relative_path).is_file())


if __name__ == "__main__":
	unittest.main()
