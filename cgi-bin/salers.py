#!/usr/bin/python3.6
# -*- coding: utf8 -*-

from navbar import nav
import mysql.connector
from yattag import Doc
doc, tag, text = Doc().tagtext()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="order",
  passwd="mysql"
)
fields = ['ncust', 'name', 'fullname', 'ipn', 'town']
ss = "SELECT " + ", ".join(fields) + " FROM saler ORDER by name"

mycursor = mydb.cursor()
mycursor.execute(ss)
myresult = mycursor.fetchall()


doc.asis('<!DOCTYPE html>')
with tag('html'):
  with tag('head'):
    doc.stag('meta', ('charset', 'UTF-8'))
    doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")
    doc.stag('link', href="../css/salers.css", rel="stylesheet")

  with tag('body', klass="container"):
    with tag('h1'):
      text('SALERS')
    with tag("table", klass="tab_cust"):
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
