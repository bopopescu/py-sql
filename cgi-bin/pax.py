#!/usr/bin/env python3
# -*- coding: utf8 -*
import mysql.connector
import requests
import re
from yattag import Doc
doc, tag, text = Doc().tagtext()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="order",
    passwd="mysql"
)
v_nsaler = 3
v_npaxv = 1
fields_pax = {'order_ID': 'pax.npaxv', 'order_N': 'pax.npax', 'order_date': 'pax.daypax',
              'order_sum': 'pax.sumpax', 'order_PDV': 'pax.pdv', 'order_custname': 'cust.name',
              'order_names': 'mast.names'}
ss = "SELECT " + ", ".join(fields_pax.values()) + \
    " FROM pax INNER JOIN cust ON pax.ncust = cust.ncust INNER JOIN mast ON pax.NNPAXB = mast.NNPAXB WHERE npaxv=" + str(v_npaxv) + \
    " AND pax.nnpaxb=" + str(v_nsaler)

print("Content-type: text/html\n")

#print(ss)
mycursor = mydb.cursor()
mycursor.execute(ss)
myresult_pax = mycursor.fetchall()

fields_paxt = {'tov': 'tov', 'ov': 'ov',
               'kol': 'kol', 'price': 'price', 'sum': 'price*kol as sum'}

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.stag('meta', ('charset', 'UTF-8'))
        doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")
        doc.stag('link', href="../css/pax.css", rel="stylesheet")

    with tag('body', klass='container'):
        with tag('form', action='customers.py', method='POST'):
            text()
        for y in myresult_pax:
            daypax = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3.\\2.\\1', str(y[2]))
            print(daypax)
            with tag('h3'):
                text("Рахунок № " + str(y[1]) + " від: " + daypax)
            with tag('div', klass='row'):
                with tag("ul", klass="saler col-xs-6"):
                    with tag('li'):
                        text("Постачальник: ")
                        text(y[6])
                    with tag('li'):
                        text("Код: \n")
                    with tag('li'):
                        text("П/З: \n")
                    with tag('li'):
                        text("Банк: \n")
                with tag('ul', klass='customer col-xs-6'):
                    with tag('li'):
                        text("  Платник: " + str(y[5]))
            ss = "SELECT " + ", ".join(fields_paxt.values()) + \
                 " FROM paxt WHERE paxt.npaxv = " + \
                 str(y[0]) + " ORDER by tov"
            mycursor = mydb.cursor()
            mycursor.execute(ss)
            myresult_paxt = mycursor.fetchall()
            with tag("table", klass="table table-bordered table-hover tab_paxt"):
                with tag('thead'):
                    with tag("tr"):
                        with tag("th"):
                            text("№")
                        for x in fields_paxt.keys():
                            with tag("th"):
                                text(x)
                i = 1
                total=0
                with tag('tbody'):
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
                        total += item
                        i += 1
                with tag('tfooter'):
                    with tag('tr'):
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('Всього:')
                        with tag('td'):
                            text(str(format(total, '>.2f')))
                    with tag('tr'):
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('ПДВ:')
                        with tag('td'):
                            text(str(format(y[4]*total/100, '>.2f')))
                    with tag('tr'):
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('')
                        with tag('td'):
                            text('Разом:')
                        with tag('td'):
                            text(str(format(total+(y[4]*total/100), '>.2f')))

print("Content-type: text/html")
print()
print(doc.getvalue())
