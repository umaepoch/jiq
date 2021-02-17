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
from PyPDF2 import PdfFileMerger, PdfFileReader,PdfFileWriter
from shutil import copyfile
import PyPDF2 

STANDARD_USERS = ("Guest", "Administrator")

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

@frappe.whitelist()
def combine(attached_to_name):
    get_merge_file_url_list = frappe.db.sql("""select pch_coc,pch_build_sheet,pch_pressure_test,pch_eu_declaration,pch_dnv_gl_product_certificate from `tabSerial No` where name=%s""",attached_to_name)
    lists=[]
    paths=[]
    path_url = '/home/mdpy27/frappe-bench/sites/site1.local/public'
    list_of_values=list(get_merge_file_url_list[0])
    Not_none_values = filter(None.__ne__, list_of_values)
    list_of_values = list(Not_none_values)
    #print(list_of_values)
    for loop in list_of_values:
        test1=path_url+loop
        lists.append(test1)
    paths=lists
    #print("paths",paths)
    path_of_file='/home/mdpy27/frappe-bench/sites/site1.local/public/files/'
    name_of_merge_pdf=attached_to_name+".pdf"
    name_of_pdf= os.path.join(path_of_file, name_of_merge_pdf)
    #print("-------------",name_of_pdf)
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
    output=name_of_pdf
    with open(output, 'wb') as out:
        pdf_writer.write(out)
        #print("test_path",out)
    frappe.msgprint(_("Single pdf File created "))
    file_url = "/files/"+attached_to_name+".pdf"
    return file_url

#jyoti
@frappe.whitelist()
def userlist(user):
    name_of_user=user
    #print("name_of_user",name_of_user)
    names= frappe.db.sql("""select user from `tabCustomer Profile` where  docstatus=1 and user='"""+user+"""' """ , as_dict=1)
    #print ("names----",names)
    return names


    

