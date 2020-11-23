# -*- coding: utf-8 -*-
# Copyright (c) 2020, Frappé and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from datetime import datetime, timedelta
import datetime

class InternalConcession(Document):
	pass

@frappe.whitelist()
def testing_api():
	return "success"



@frappe.whitelist()
def serial_no(work_order):
	serial_no_list= frappe.db.sql("""select sed.serial_no from `tabStock Entry Detail` sed,`tabStock Entry` se where sed.parent=se.name and se.work_order='"""+work_order+"""'  and sed.s_warehouse is NULL  and se.purpose="Manufacture" and se.docstatus!=2  """, as_dict=1)
	#print("items",items)
	return serial_no_list


