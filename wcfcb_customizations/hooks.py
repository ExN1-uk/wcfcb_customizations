app_name = "wcfcb_customizations"
app_title = "Wcfcb Customizations"
app_publisher = "ExN"
app_description = "WCFCB ERP Customizations - Exported from DB backup 20251211_000018"
app_email = "marcques@exn1.uk"
app_license = "mit"

# Apps
# ------------------

required_apps = ["frappe", "erpnext", "hrms"]

# Fixtures - All customizations to be exported/imported
# ------------------------------------------------------
fixtures = [
    # Custom Fields on standard DocTypes
    "Custom Field",

    # Property modifications on standard fields
    "Property Setter",

    # Server-side Python scripts
    "Server Script",

    # Client-side JavaScript scripts
    "Client Script",

    # Workflow definitions
    "Workflow",
    "Workflow State",
    "Workflow Action Master",

    # Custom Roles
    {"dt": "Role", "filters": [
        ["name", "not in", [
            "System Manager", "Administrator", "Guest", "All",
            "Blogger", "Website Manager", "Translator", "Script Manager",
            "Report Builder", "Analytics", "Newsletter Manager",
            "Knowledge Base Contributor", "Knowledge Base Editor",
            "Desk User", "Inbox User", "Prepared Report User"
        ]]
    ]},

    # Notifications/Alerts
    "Notification",

    # Custom Reports
    {"dt": "Report", "filters": [["is_standard", "=", "No"]]},

    # Print Formats
    {"dt": "Print Format", "filters": [["standard", "=", "No"]]},

    # Letter Heads
    "Letter Head",

    # Email Templates
    "Email Template",

    # Custom DocTypes (created via UI)
    {"dt": "DocType", "filters": [["custom", "=", 1]]},

    # Dashboard Charts
    {"dt": "Dashboard Chart", "filters": [["is_standard", "=", 0]]},

    # Number Cards
    {"dt": "Number Card", "filters": [["is_standard", "=", 0]]},

    # Custom Workspaces (module filter for custom modules)
    {"dt": "Workspace", "filters": [["module", "in", [
        "ExN", "WCFCB ZM", "WCFCB CRM", "ZRA INTERGRATION", "Accounts", "Assets"
    ]]]},
]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "wcfcb_customizations",
# 		"logo": "/assets/wcfcb_customizations/logo.png",
# 		"title": "Wcfcb Customizations",
# 		"route": "/wcfcb_customizations",
# 		"has_permission": "wcfcb_customizations.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wcfcb_customizations/css/wcfcb_customizations.css"
# app_include_js = "/assets/wcfcb_customizations/js/wcfcb_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/wcfcb_customizations/css/wcfcb_customizations.css"
# web_include_js = "/assets/wcfcb_customizations/js/wcfcb_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "wcfcb_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "wcfcb_customizations/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "wcfcb_customizations.utils.jinja_methods",
# 	"filters": "wcfcb_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "wcfcb_customizations.install.before_install"
# after_install = "wcfcb_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "wcfcb_customizations.uninstall.before_uninstall"
# after_uninstall = "wcfcb_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "wcfcb_customizations.utils.before_app_install"
# after_app_install = "wcfcb_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "wcfcb_customizations.utils.before_app_uninstall"
# after_app_uninstall = "wcfcb_customizations.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wcfcb_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wcfcb_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"wcfcb_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"wcfcb_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wcfcb_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"wcfcb_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "wcfcb_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wcfcb_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wcfcb_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["wcfcb_customizations.utils.before_request"]
# after_request = ["wcfcb_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["wcfcb_customizations.utils.before_job"]
# after_job = ["wcfcb_customizations.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"wcfcb_customizations.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

