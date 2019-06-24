#!/usr/bin/env python3
# -*- coding: utf8 -*
from navbar import nav
import mysql.connector
import requests
from yattag import Doc
doc, tag, text = Doc().tagtext()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="order",
    passwd="mysql"
)
fields_pax = {'order_ID':'pax.npaxv', 'order_N':'pax.npax', 'order_date':'pax.daypax',
              'order_sum':'pax.sumpax', 'order_PDV':'pax.pdv', 'order_custname':'cust.name'}
ss = "SELECT " + ", ".join(fields_pax.values()) + \
    " FROM pax INNER JOIN cust ON pax.ncust = cust.ncust ORDER by daypax"
print(ss)
#print(fields_pax['order_ID'])
mycursor = mydb.cursor()
mycursor.execute(ss)
myresult_pax = mycursor.fetchall()

fields_paxt = {'tov':'paxt.tov', 'ov':'paxt.ov', 'kol':'paxt.kol', 'price':'paxt.price'}

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.stag('meta', ('charset', 'UTF-8'))
        doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")
        doc.stag('link', href="../css/orders.css", rel="stylesheet")

    with tag('body', klass='container'):
        with tag('h1'):
            text('Orders')
        with tag('form', action='customers.py', method='POST'):
            with tag('input', type='submit', value='CUSTOMERS', klass='btn btn-primary'):
                text()
        for y in myresult_pax:
            with tag('h2'):
                text("Рахунок № " + str(y[1]) + " від: " + str(y[2]))
                text("  Платник: " + str(y[5]))
            ss = "SELECT " + ", ".join(fields_paxt.values()) + \
                 " FROM paxt WHERE paxt.npaxv = " + \
                 str(y[0]) + " ORDER by tov"
            mycursor = mydb.cursor()
            mycursor.execute(ss)
            myresult_paxt = mycursor.fetchall()
            with tag("table", klass="table table-bordered table-hover tab_paxt"):
                with tag("tr"):
                    with tag("th"):
                        text("№")
                    for x in fields_paxt.keys():
                        with tag("th"):
                            text(x)
                    with tag('th'):
                        text('sum')
                i = 1
                for x in myresult_paxt:
                    with tag("tr"):
                        with tag("td"):
                            text(str(i))
                        for item in x:
                            st = str(item)
                            if type(item).__name__ == 'Decimal':
                                st = format(item, '>.2f')
                            with tag("td"):
                                text(str(st))
                        sum = x[2] * x[3]
                        with tag("td"):
                            text(str(format(sum, '>10.2f')))
                    i += 1

from navbar import nav
print("Content-type: text/html")
print()
print(doc.getvalue())
nav()
