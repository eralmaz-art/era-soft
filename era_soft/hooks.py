"""Frappe application metadata and extension points.

Keep hooks additive. Any override of an ERPNext class or whitelisted method
requires an architecture decision record and regression coverage.
"""

app_name = "era_soft"
app_title = "ERA SOFT"
app_publisher = "ERA Group"
app_description = "Business operating platform for ERA Group"
app_email = ""
app_license = "Proprietary"
app_version = "0.5.1"

required_apps = ["erpnext"]

app_logo_url = "/assets/era_soft/images/era-soft-mark.svg"
app_home = "/desk/era-soft"

add_to_apps_screen = [
	{
		"name": "era_soft",
		"logo": app_logo_url,
		"title": app_title,
		"route": app_home,
	}
]

app_include_css = ["/assets/era_soft/css/era_soft.css?v=0.5.1"]

doctype_js = {
	"Project": "public/js/project.js",
}

# Workflow roles must exist before the standard DocType permissions are synced.
before_migrate = [
	"era_soft.setup.construction_mvp.ensure_construction_roles",
]

# Site-level branding is applied conservatively after schema/configuration sync.
# Existing custom names and logos are preserved.
after_migrate = [
	"era_soft.setup.visual_baseline.apply_visual_baseline",
	"era_soft.setup.localization.apply_russian_localization",
	"era_soft.setup.construction_mvp.apply_construction_mvp",
]
