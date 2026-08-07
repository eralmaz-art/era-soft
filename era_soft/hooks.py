"""Frappe application metadata and extension points.

Keep hooks additive. Any override of an ERPNext class or whitelisted method
requires an architecture decision record and regression coverage.
"""

app_name = "era_soft"
app_title = "ERA SOFT"
app_publisher = "ERA Group"
app_description = "Construction and ready-mix concrete operations for ERA Group"
app_email = ""
app_license = "Proprietary"
app_version = "0.1.0"

required_apps = ["erpnext"]

# Deliberately empty during the foundation phase. Business hooks are introduced
# only after the ERPNext fit-gap decision is recorded.
