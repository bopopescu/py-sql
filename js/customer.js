  $(document).ready(function () {
    $('.tab_cust tbody tr').dblclick(function () {
     $('.modale').toggle();

      ss = this.getElementsByTagName('td')[3].innerHTML;
    //  ss = $(this)[0].children[3].innerHTML; // .cells[4].text();
      console.log(ss);
/*      $.ajax({
        method: "GET",
        url: "/js/test.js",
        dataType: "script"
      });*/
      $.ajax({
        method: 'GET',
        url: '/js/test.js',
        data: { name: 'Ivan' }})
        .done(function (data) {
          alert(data);
        })
        .fail(function () {
          alert('error');
        });
  });
});