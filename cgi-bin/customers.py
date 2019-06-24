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
ss = "SELECT * FROM cust ORDER by name"

mycursor = mydb.cursor()
mycursor.execute(ss)
myresult = mycursor.fetchall()

mycursor.execute('SHOW columns FROM cust')
col_count = 15
columns = mycursor.fetchmany(col_count)

doc.asis('<!DOCTYPE html>')
with tag('html'):
  with tag('head'):
    doc.stag('meta', ('charset', 'UTF-8'))
    doc.stag('link', href="../css/customers.css", rel="stylesheet")
    doc.stag('link', href="../css/bootstrap.css", rel="stylesheet")
    with tag('script', src="/js/jquery.js"):
      text()
    with tag('script', src="/js/customer.js"):
      text()
  with tag('body'):
    with tag('h1'):
      text('CUSTOMERS')

    with tag("table", klass="tab_cust table table-bordered table-hover"):
      with tag('thead'):
        with tag('tr'):
          for x in columns:
            with tag('th'):
              text(x[0])
      for x in myresult:
        with tag("tr"):
          i = 0
          while i < col_count:
            with tag("td"):
              text(str(x[i]))
              i += 1

from navbar import nav
print("Content-type: text/html")
print("charset=utf-8\n\n")
print()
print(doc.getvalue())
nav()
print('''<div id="id01" class="modale">
  <span onclick="document.getElementById('id01').style.display='none'"
class="close" title="Close Modal">&times;</span>

  <!-- Modal Content -->
  <form class="modal-content animate" action="sklad.py">

    <div class="cont">''')

print('''
      <label for="uname"><b>Username</b></label>
      <input type="text" placeholder="Enter Username" name="uname" >

      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="psw" >

      <button type="submit">Login</button>
      <label>
        <input type="checkbox" checked="checked" name="remember"> Remember me
      </label>
    </div>

    <div class="cont" style="background-color:#f1f1f1">
      <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
      <span class="psw">Forgot <a href="#">password?</a></span>
    </div>
  </form>
</div>''')
