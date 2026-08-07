"""Apply and restore the ERA SOFT Russian-language baseline."""

from __future__ import annotations

import frappe


RUSSIAN = "ru"
ENGLISH = "en"


def apply_russian_localization() -> None:
	"""Make Russian the site default while preserving later user preferences."""

	previous_system_language = frappe.db.get_single_value("System Settings", "language")
	changed = False

	if previous_system_language in {None, "", ENGLISH, RUSSIAN} and previous_system_language != RUSSIAN:
		frappe.db.set_single_value("System Settings", "language", RUSSIAN)
		changed = True

	# The prepared local site is operated through Administrator. Move that user
	# to Russian only on the first transition from the former system language.
	# A developer who later selects English will not be reset on every migration.
	if previous_system_language != RUSSIAN and frappe.db.exists("User", "Administrator"):
		administrator_language = frappe.db.get_value("User", "Administrator", "language")
		if administrator_language in {None, "", previous_system_language}:
			frappe.db.set_value(
				"User",
				"Administrator",
				"language",
				RUSSIAN,
				update_modified=False,
			)
			changed = True

	if changed:
		frappe.clear_cache()


def restore_russian_localization() -> None:
	"""Restore English only where the ERA Russian baseline still owns the value."""

	changed = False
	if frappe.db.get_single_value("System Settings", "language") == RUSSIAN:
		frappe.db.set_single_value("System Settings", "language", ENGLISH)
		changed = True

	if (
		frappe.db.exists("User", "Administrator")
		and frappe.db.get_value("User", "Administrator", "language") == RUSSIAN
	):
		frappe.db.set_value(
			"User",
			"Administrator",
			"language",
			ENGLISH,
			update_modified=False,
		)
		changed = True

	if changed:
		frappe.clear_cache()
