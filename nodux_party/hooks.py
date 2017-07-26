# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nodux_party"
app_title = "Nodux Party"
app_publisher = "NODUX"
app_description = "Custom Party"
app_icon = "octicon octicon-file-directory"
app_color = "dark red"
app_email = "tatianaq@nodux.ec"
app_license = "MIT"
#fixtures = ['Customer', 'Supplier']

hooks = ["nombre_de_contacto", "fecha_de_registro", "fecha_de_nacimiento",
    "comercial_name", "email", "mobile", "more_information", "province", "country",
    "phone", "street", "address_and_contacts", "is_supplier", "sca3", "sca2", "ssa1"
    "sc1", "salto_3", "salto_2", "salto_columna", "salto_1"]

# doctype_js = {
#         "Customer": "nodux_party/customer.js"
# }
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nodux_party/css/nodux_party.css"
# app_include_js = "/assets/nodux_party/js/nodux_party.js"

# include js, css files in header of web template
# web_include_css = "/assets/nodux_party/css/nodux_party.css"
# web_include_js = "/assets/nodux_party/js/nodux_party.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nodux_party.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nodux_party.install.before_install"
# after_install = "nodux_party.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nodux_party.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Customer": {
# 		"validate": "nodux_party.customer.validate_tax_id",
#         "validate": "nodux_party.customer.create_supplier",
#         "validate": "nodux_party.customer.validate_email",
#         "validate": "nodux_one.customer.remove_spaces"
# 	}
# }


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nodux_party.tasks.all"
# 	],
# 	"daily": [
# 		"nodux_party.tasks.daily"
# 	],
# 	"hourly": [
# 		"nodux_party.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nodux_party.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nodux_party.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nodux_party.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nodux_party.event.get_events"
# }
