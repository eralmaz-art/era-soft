from __future__ import annotations

import csv
import json
import pathlib
import re
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

	def test_russian_translation_layer_has_unique_sources(self) -> None:
		translation_path = ROOT / "era_soft" / "translations" / "ru.csv"
		with translation_path.open(encoding="utf-8", newline="") as translation_file:
			rows = list(csv.reader(translation_file))
		sources = [row[0] for row in rows]
		self.assertEqual(len(sources), len(set(sources)))
		self.assertTrue(all(len(row) in {2, 3} for row in rows))

	def test_russian_terminology_matches_approved_terms(self) -> None:
		translation_path = ROOT / "era_soft" / "translations" / "ru.csv"
		with translation_path.open(encoding="utf-8", newline="") as translation_file:
			translations = {row[0]: row[1] for row in csv.reader(translation_file)}

		self.assertEqual(
			{source: translations[source] for source in self.APPROVED_RUSSIAN_TERMS},
			self.APPROVED_RUSSIAN_TERMS,
		)

	def test_every_custom_workspace_label_has_a_russian_translation(self) -> None:
		translation_path = ROOT / "era_soft" / "translations" / "ru.csv"
		with translation_path.open(encoding="utf-8", newline="") as translation_file:
			translated_sources = {row[0] for row in csv.reader(translation_file)}

		visible_sources: set[str] = set()
		for workspace_path in sorted((ROOT / "era_soft").glob("**/workspace/**/*.json")):
			workspace = json.loads(workspace_path.read_text(encoding="utf-8"))
			visible_sources.add(workspace["title"])
			visible_sources.update(link["label"] for link in workspace.get("links", []))
			for block in json.loads(workspace["content"]):
				if card_name := block.get("data", {}).get("card_name"):
					visible_sources.add(card_name)
				if text := block.get("data", {}).get("text"):
					visible_sources.add(re.sub(r"<[^>]+>", "", text))

		sidebar = json.loads(
			(ROOT / "era_soft" / "workspace_sidebar" / "construction.json").read_text(
				encoding="utf-8"
			)
		)
		visible_sources.update(item["label"] for item in sidebar["items"])
		visible_sources.discard("ERA SOFT")

		self.assertEqual(visible_sources - translated_sources, set())

	APPROVED_RUSSIAN_TERMS = {
		"Dashboard": "Главная",
		"Construction": "Строительство",
		"Procurement": "Закупки",
		"Finance": "Финансы",
		"Projects": "Проекты",
		"Suppliers": "Поставщики",
		"Employees": "Сотрудники",
		"Reports": "Отчеты",
		"Settings": "Настройки",
		"Customer": "Клиент",
		"Supplier": "Поставщик",
		"Purchase Order": "Заказ на закупку",
		"Payment Entry": "Оплата",
		"Cost": "Себестоимость",
		"Project": "Объект",
		"Account": "Статья затрат",
	}


if __name__ == "__main__":
	unittest.main()
