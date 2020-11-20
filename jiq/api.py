from __future__ import unicode_literals
import frappe
from frappe import _, throw, msgprint, utils
from frappe.utils import cint, flt, cstr, comma_or, getdate, add_days, getdate, rounded, date_diff, money_in_words
from frappe.model.mapper import get_mapped_doc
from frappe.model.naming import make_autoname
from erpnext.utilities.transaction_base import TransactionBase
from erpnext.accounts.party import get_party_account_currency
from frappe.desk.notifications import clear_doctype_notifications
from datetime import datetime
from datetime import date
import sys
import os
import operator
import frappe
import json
import time
import math
import base64
import ast
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from frappe.cache_manager import clear_user_cache,clear_global_cache
from frappe.sessions import Session, clear_sessions

@frappe.whitelist()
def testing_api():
	return "success"

#jyoti
@frappe.whitelist()
def item_query_quality_inspection(parent):
	items= frappe.db.sql("""select item_code from `tabWork Order Item` where parent='"""+parent+"""'  """, as_dict=1)
	#print("items",items)
	return items

#jyoti
@frappe.whitelist()
def serial_no(work_order):
	serial_no_list= frappe.db.sql("""select sed.serial_no from `tabStock Entry Detail` sed,`tabStock Entry` se where sed.parent=se.name and se.work_order='"""+work_order+"""'  and sed.s_warehouse is NULL  and se.purpose="Manufacture" and se.docstatus!=2  """, as_dict=1)
	#print("items",items)
	return serial_no_list

#jyoti
@frappe.whitelist()
def serial_no_list(work_order):
	serial_no= frappe.db.sql("""select sn.serial_no from `tabStock Entry Detail` sed,`tabSerial No` sn,`tabStock Entry` se where sed.parent=se.name and se.work_order='"""+work_order+"""' and sed.s_warehouse is NULL and sn.purchase_document_no=se.name and se.purpose="Manufacture"  """, as_dict=1)
	#print("items",items)
	res = [ sub['serial_no'] for sub in serial_no ] 
	return res
