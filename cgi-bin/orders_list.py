#!/usr/bin/python3.6
# -*- coding: utf8 -*-
from navbar import nav
import datetime
import mysql.connector
from yattag import Doc
doc, tag, text = Doc().tagtext()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="order",
  passwd="mysql"
)
pax_fields = ['pax.npaxv', 'pax.npax', 'pax.daypax', 'pax.sumpax', 'pax.pdv', 'cust.name']
paxt_fields = ['paxt.npaxv', 'paxt.tov', 'paxt.ov', 'paxt.kol', 'paxt.price']
ss = "SELECT " + ", ".join(pax_fields) + " FROM pax INNER JOIN cust ON pax.ncust = cust.ncust ORDER by daypax"
print(ss)
mycursor = mydb.cursor()
mycursor.execute(ss)
pax_result = mycursor.fetchall()

ss = "SELECT " + ", ".join(paxt_fields) + " FROM paxt INNER JOIN pax ON pax.npaxv = paxt.npaxv ORDER by tov"
mycursor.execute(ss)
paxt_result = mycursor.fetchall()
print(paxt_result)



doc.asis('<!DOCTYPE html>')
with tag('html'):
  with tag('head'):
    doc.stag('meta', ('charset', 'UTF-8'))
    doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")
    doc.stag('link', href="../css/orders_list.css", rel="stylesheet")

  with tag('body'):
    with tag('h1'):
      text('Orders list')
    with tag("table", klass="tab_orders_list table table-bordered table-hover"):
      with tag("thead", klass="fixed_top"):
        with tag("tr"):
          i = 1
          while i <= len(pax_fields):
            with tag("th"):
              text(pax_fields[i-1])
            i += 1
      with tag("tbody"):
        for x in pax_result:
          with tag("tr"):
            for item in x:
              with tag("td"):
                text(str(item))

from navbar import nav
print("Content-type: text/html")
print()
print(doc.getvalue())
nav()
