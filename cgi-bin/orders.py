#!/usr/bin/env python3
# -*- coding: utf8 -*
import cgi
import cgitb
cgitb.enable()
import mysql.connector
from yattag import Doc
doc, tag, text = Doc().tagtext()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="order",
    passwd="mysql"
)
fields_pax = ['pax.npaxv', 'pax.npax', 'pax.daypax',
              'pax.sumpax', 'pax.pdv', 'cust.name']
ss = "SELECT " + ", ".join(fields_pax) + \
    " FROM pax INNER JOIN cust ON pax.ncust = cust.ncust"

input_data = cgi.FieldStorage()
print("Content-type: text/html")
print()

s = input_data.getfirst("filter", "NO")

if s != 'NO' :
    ss = ss + " " + s

print(ss)
mycursor = mydb.cursor()
mycursor.execute(ss)
myresult_pax = mycursor.fetchall()

fields_paxt = ['paxt.tov', 'paxt.ov', 'paxt.kol', 'paxt.price']

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.stag('meta', ('charset', 'UTF-8'))
        doc.stag('link', href="../css/orders_list.css", rel="stylesheet")
        doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")

    with tag('body'):
        with tag('h1'):
            text('Orders')

        for y in myresult_pax:
            with tag('h2'):
                text("Order N " + str(y[1]) + " date: " + str(y[2]))
                text("  customer: " + str(y[5]))
            ss = "SELECT " + ", ".join(fields_paxt) + \
                 " FROM paxt WHERE paxt.npaxv = " + \
                 str(y[0]) + " ORDER by tov"
            mycursor = mydb.cursor()
            mycursor.execute(ss)
            myresult_paxt = mycursor.fetchall()
            with tag("table", klass="item_list"):
                with tag("tr"):
                    i = 0
                    with tag("th"):
                        text("№")
                    while i < len(fields_paxt):
                        with tag("th"):
                            text(fields_paxt[i])
                            i += 1
                i = 1
                for x in myresult_paxt:
                    with tag("tr"):
                        with tag("td"):
                            text(str(i))
                        for item in x:
                            with tag("td"):
                                text(str(item))
                        i += 1
                        sum = x[2] * x[3]
                        with tag("td"):
                            text(str(sum))
from navbar import nav
print("Content-type: text/html")
print()
print(doc.getvalue())
nav()
