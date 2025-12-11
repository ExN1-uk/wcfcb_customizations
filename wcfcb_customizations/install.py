"""
Installation and migration hooks for wcfcb_customizations.
Ensures all DocTypes bundled with this app have correct module assignments.
"""
import os
import json
import frappe


def after_migrate():
    """
    Called after bench migrate.
    Fixes module assignments for all DocTypes bundled with this app.
    """
    fix_doctype_modules()


def after_install():
    """
    Called after app installation.
    Fixes module assignments for all DocTypes bundled with this app.
    """
    fix_doctype_modules()


def fix_doctype_modules():
    """
    Scan all DocType JSON files in this app and ensure the database
    module assignment matches the JSON file's module.
    
    This prevents "FileNotFoundError" when Frappe looks for DocType
    files in the wrong app based on incorrect module assignments.
    """
    app_path = frappe.get_app_path("wcfcb_customizations")
    doctype_base = os.path.join(app_path, "wcfcb_customizations", "doctype")
    
    if not os.path.exists(doctype_base):
        return
    
    fixed_count = 0
    
    for dt_folder in os.listdir(doctype_base):
        dt_path = os.path.join(doctype_base, dt_folder)
        if not os.path.isdir(dt_path):
            continue
            
        json_file = os.path.join(dt_path, f"{dt_folder}.json")
        if not os.path.exists(json_file):
            continue
        
        try:
            with open(json_file, "r") as f:
                dt_data = json.load(f)
            
            dt_name = dt_data.get("name")
            json_module = dt_data.get("module", "WCFCB Customizations")
            
            if not dt_name:
                continue
            
            # Check current DB module
            db_module = frappe.db.get_value("DocType", dt_name, "module")
            
            if db_module and db_module != json_module:
                # Fix the module assignment
                frappe.db.set_value("DocType", dt_name, "module", json_module, update_modified=False)
                fixed_count += 1
                frappe.logger().info(f"Fixed module for {dt_name}: {db_module} -> {json_module}")
        
        except Exception as e:
            frappe.logger().error(f"Error fixing module for {dt_folder}: {e}")
    
    if fixed_count > 0:
        frappe.db.commit()
        print(f"wcfcb_customizations: Fixed module assignments for {fixed_count} DocTypes")

