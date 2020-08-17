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


#jyoti
@frappe.whitelist()
def item_query_quality_inspection(parent):
    items= frappe.db.sql("""select item_code from `tabWork Order Item` where parent='"""+parent+"""'  """, as_dict=1)
    #print("items",items)
    return items
