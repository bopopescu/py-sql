def nav():
  print('''<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container-fluid">
  <div class="navbar-header">
      <a class="navbar-brand" href="http://localhost:4000/">HOME</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="/cgi-bin/customers.py">CUSTOMERS</a></li>
      <li><a href="/cgi-bin/salers.py">SALERS</a></li>
      <li><a href="/cgi-bin/orders_list.py">ORDERS LIST</a></li>
      <li><a href="/cgi-bin/orders-dict.py">ORDERS DICT</a></li>
      <li><a href="/cgi-bin/orders.py">ORDERS</a></li>
      <li><a href="/cgi-bin/sklad.py">SKLAD</a></li>
      <li><a href="http://localhost:4000/1.html">RUN</a></li>
    </ul>
  </div>
</nav>''')
