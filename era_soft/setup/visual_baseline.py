"""Apply and restore the upgrade-safe ERA SOFT visual baseline."""

from __future__ import annotations

import frappe


ERA_APP_NAME = "ERA SOFT"
ERA_APP = "era_soft"
ERA_LOGO = "/assets/era_soft/images/era-soft-logo.svg"
ERA_MARK = "/assets/era_soft/images/era-soft-mark.svg"

_DEFAULT_NAMES = {None, "", "Frappe", "ERPNext", ERA_APP_NAME}
_MANAGED_ASSETS = {None, "", ERA_LOGO, ERA_MARK}
_ERPNEXT_ROOT_ICONS = ("Organization", "Accounting", "Subcontracting", "ERPNext Settings")


def _set_single_if_managed(
	doctype: str,
	fieldname: str,
	value: str,
	managed_values: set[str | None],
) -> bool:
	current = frappe.db.get_single_value(doctype, fieldname)
	if current not in managed_values:
		return False
	if current == value:
		return False
	frappe.db.set_single_value(doctype, fieldname, value)
	return True


def _set_value_if_managed(
	doctype: str,
	name: str,
	fieldname: str,
	value: str | int,
	managed_values: set[str | int | None],
) -> bool:
	current = frappe.db.get_value(doctype, name, fieldname)
	if current not in managed_values or current == value:
		return False
	frappe.db.set_value(doctype, name, fieldname, value, update_modified=False)
	return True


def apply_visual_baseline() -> None:
	"""Set ERA defaults without overwriting a site operator's custom branding."""

	changed = False
	changed |= _set_single_if_managed("Website Settings", "app_name", ERA_APP_NAME, _DEFAULT_NAMES)
	changed |= _set_single_if_managed("Website Settings", "title_prefix", ERA_APP_NAME, _DEFAULT_NAMES)
	changed |= _set_single_if_managed("Website Settings", "app_logo", ERA_LOGO, _MANAGED_ASSETS)
	changed |= _set_single_if_managed("Website Settings", "splash_image", ERA_MARK, _MANAGED_ASSETS)
	changed |= _set_single_if_managed("Website Settings", "favicon", ERA_MARK, _MANAGED_ASSETS)
	changed |= _set_single_if_managed("System Settings", "app_name", ERA_APP_NAME, _DEFAULT_NAMES)
	changed |= _set_single_if_managed(
		"System Settings",
		"default_app",
		ERA_APP,
		{None, "", "erpnext", ERA_APP},
	)
	# ERPNext v16 ships its app tile hidden, which promotes every child module to
	# the root desktop. Showing the parent groups those modules behind one tile.
	changed |= _set_value_if_managed("Desktop Icon", "ERPNext", "hidden", 0, {0, 1})
	for icon_name in _ERPNEXT_ROOT_ICONS:
		changed |= _set_value_if_managed(
			"Desktop Icon",
			icon_name,
			"parent_icon",
			"ERPNext",
			{None, "", "ERPNext"},
		)

	if changed:
		frappe.clear_cache()


def restore_visual_baseline() -> None:
	"""Remove only values owned by this baseline, preserving later customizations."""

	changed = False
	changed |= _set_single_if_managed(
		"Website Settings",
		"app_name",
		"Frappe",
		{ERA_APP_NAME},
	)
	changed |= _set_single_if_managed(
		"Website Settings",
		"title_prefix",
		"",
		{ERA_APP_NAME},
	)
	changed |= _set_single_if_managed(
		"Website Settings",
		"app_logo",
		"",
		{ERA_LOGO, ERA_MARK},
	)
	changed |= _set_single_if_managed(
		"Website Settings",
		"splash_image",
		"",
		{ERA_LOGO, ERA_MARK},
	)
	changed |= _set_single_if_managed(
		"Website Settings",
		"favicon",
		"",
		{ERA_LOGO, ERA_MARK},
	)
	changed |= _set_single_if_managed(
		"System Settings",
		"app_name",
		"Frappe",
		{ERA_APP_NAME},
	)
	changed |= _set_single_if_managed(
		"System Settings",
		"default_app",
		"",
		{ERA_APP},
	)
	changed |= _set_value_if_managed("Desktop Icon", "ERPNext", "hidden", 1, {0})
	for icon_name in _ERPNEXT_ROOT_ICONS:
		changed |= _set_value_if_managed(
			"Desktop Icon",
			icon_name,
			"parent_icon",
			"",
			{"ERPNext"},
		)

	if changed:
		frappe.clear_cache()
