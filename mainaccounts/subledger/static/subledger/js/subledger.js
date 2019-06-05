function Function_object_code() {
  var x = document.getElementById("form.function_id").selectedIndex;
  var y = document.getElementById("form.function_id").options;
  var a = y[x].text;
  var splitThis = a.split("-");
  var x1 = document.getElementById("form.object_id").selectedIndex;
  var y1 = document.getElementById("form.object_id").options;
  var a1 = y1[x1].text;
  var splitThis1 = a1.split("-");
  var alib =a1.substr(0, 1);

  if(alib=='3' || alib=='4') 
  {

    $("#dvopenbal").show();
    $("#dvopenbaldate").show();
    
  } else {
      $("#dvopenbal").hide();
      $("#dvopenbaldate").hide();
}
   
  if(x1!="0" && x!="0")
  {
  document.getElementById("subledger_code").value = splitThis[0]+splitThis1[0];
  }
  }




  $(document).on('click', '#btn-submit', function(e) {
  e.preventDefault();
      var x = document.getElementById("form.function_id").selectedIndex;
      var x1 = document.getElementById("form.object_id").selectedIndex;
      var x2 = document.getElementById("form.lookupdet_bug").selectedIndex;
      var x3 = document.getElementById("form.budget_provion_required").selectedIndex;
      var x4 = document.getElementById("subledger_desc").value;
      var x5 = document.getElementById("form.status").selectedIndex;
        if(x1!="0" && x!="0" && x2!="0"  && x4!="" && x5!="0")
        {
          swal({
          title: 'Save Successfully ',
          }).then(function (result) {
          $('#myForm').submit();
          });
        }
        else
        {
          swal({
          title: 'Fields Empty!!',
          text: "Please check the missing fields!!",
          icon:"warning",
          button: "Ok",
          });
        }
  });