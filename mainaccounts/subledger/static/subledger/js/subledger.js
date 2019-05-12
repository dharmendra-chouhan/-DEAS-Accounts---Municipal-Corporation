// $(function () {

//   /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-Subledger_master .modal-content").html("");
        $("#modal-Subledger_master").modal("show");
      },
      success: function (data) {
        $("#modal-Subledger_master .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#Subledger_master-table tbody").html(data.html_Subledger_master_list);
          $("#modal-Subledger_master").modal("hide");
        }
        else {
          $("#modal-Subledger_master .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create Subledger_master
  $(".js-create-Subledger_master").click(loadForm);
  $("#modal-Subledger_master").on("submit", ".js-Subledger_master-create-form", saveForm);

  // Update Subledger_master
  // $("#Subledger_master-table").on("click", ".js-update-Subledger_master", loadForm);
  // $("#modal-Subledger_master").on("submit", ".js-Subledger_master-update-form", saveForm);

  // Delete Subledger_master
  $("#delbtn").on("click", ".js-delete-Subledger_master", loadForm);
  $("#modal-Subledger_master").on("submit", ".js-Subledger_master-delete-form", saveForm);

// });