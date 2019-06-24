#!/usr/bin/python3.6
# -*- coding: utf8 -*-

import mysql.connector
from yattag import Doc
doc, tag, text = Doc().tagtext()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="order",
  passwd="mysql"
)
fields = ['name', 'fullname', 'ipn', 'sity']
ss = "SELECT * FROM sklad ORDER by gr"

mycursor = mydb.cursor()
mycursor.execute(ss)
myresult = mycursor.fetchall()


doc.asis('<!DOCTYPE html>')
with tag('html'):
  with tag('head'):
    doc.stag('meta', ('charset', 'UTF-8'))
    doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")

  with tag('body'):
    with tag('h1'):
      text('СКЛАД')
    with tag("table", klass="tab_sklad table table-bordered table-hover"):
      for x in myresult:
        with tag("tr"):
          for item in x:
            with tag("td"):
              text(str(item))

from navbar import nav
print("Content-type: text/html")
print("charset=utf-8\n\n")
print()
print(doc.getvalue())
nav()
