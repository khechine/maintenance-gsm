from . import __version__ as app_version

app_name = "maintenance_gsm"
app_title = "Maintenance GSM"
app_publisher = "Your Name"
app_description = "App for mobile phone repair workshops"
app_email = "your.email@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/maintenance_gsm/css/maintenance_gsm.css"
# app_include_js = "/assets/maintenance_gsm/js/maintenance_gsm.js"

# include js, css files in header of web template
# web_include_css = "/assets/maintenance_gsm/css/maintenance_gsm.css"
# web_include_js = "/assets/maintenance_gsm/js/maintenance_gsm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "maintenance_gsm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Reception Appareil": "public/js/reception_appareil.js",
    "Diagnostic Technique": "public/js/diagnostic_technique.js",
    "Ordre Reparation": "public/js/ordre_reparation.js"
}
doctype_list_js = {"Reception Appareil": "public/js/reception_appareil_list.js"}
doctype_tree_js = {}
doctype_calendar_js = {}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "maintenance_gsm/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "maintenance_gsm.utils.jinja_methods",
#	"filters": "maintenance_gsm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "maintenance_gsm.install.before_install"
# after_install = "maintenance_gsm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "maintenance_gsm.uninstall.before_uninstall"
# after_uninstall = "maintenance_gsm.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "maintenance_gsm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Reception Appareil": {
        "on_submit": "maintenance_gsm.maintenance_gsm.doctype.reception_appareil.reception_appareil.ReceptionAppareil.send_notification"
    },
    "Diagnostic Technique": {
        "on_update": "maintenance_gsm.maintenance_gsm.doctype.diagnostic_technique.diagnostic_technique.DiagnosticTechnique.update_reception_status",
        "on_update": "maintenance_gsm.maintenance_gsm.doctype.diagnostic_technique.diagnostic_technique.DiagnosticTechnique.create_ordre_reparation_if_not_exists"
    },
    "Ordre Reparation": {
        "on_update": "maintenance_gsm.maintenance_gsm.doctype.ordre_reparation.ordre_reparation.OrdreReparation.create_sales_invoice",
        "on_update": "maintenance_gsm.maintenance_gsm.doctype.ordre_reparation.ordre_reparation.OrdreReparation.update_reception_status",
        "before_submit": "maintenance_gsm.maintenance_gsm.doctype.ordre_reparation.ordre_reparation.OrdreReparation.before_submit"
    },
    "Livraison Atelier": {
        "on_submit": "maintenance_gsm.maintenance_gsm.doctype.livraison_atelier.livraison_atelier.LivraisonAtelier.update_reception_status"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"maintenance_gsm.tasks.all"
#	],
#	"daily": [
#		"maintenance_gsm.tasks.daily"
#	],
#	"hourly": [
#		"maintenance_gsm.tasks.hourly"
#	],
#	"weekly": [
#		"maintenance_gsm.tasks.weekly"
#	]
#	"monthly": [
#		"maintenance_gsm.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "maintenance_gsm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "maintenance_gsm.event.get_events"
# }
#
# each overriding function accepts a `data` parameter;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "maintenance_gsm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# automatically notifiy all clients who are affected by any change

# on_request = [
#	{"fn": "method", "filter": "doctype", "value": "leave_application", "validate": True},
#	]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_4}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_5}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"maintenance_gsm.auth.validate"
# ]