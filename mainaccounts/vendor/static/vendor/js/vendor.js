$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-vendor .modal-content").html("");
        $("#modal-vendor").modal("show");
      },
      success: function (data) {
        $("#modal-vendor .modal-content").html(data.html_form);
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
          $("#vendor-table tbody").html(data.html_vendor_list);
          $("#modal-vendor").modal("hide");
        }
        else {
          $("#modal-vendor .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create vendor
  $(".js-create-vendor").click(loadForm);
  $("#modal-vendor").on("submit", ".js-vendor-create-form", saveForm);

  // Update vendor
  $("#vendor-table").on("click", ".js-update-vendor", loadForm);
  $("#modal-vendor").on("submit", ".js-vendor-update-form", saveForm);

  // Delete vendor
  $("#vendor-table").on("click", ".js-delete-vendor", loadForm);
  $("#modal-vendor").on("submit", ".js-vendor-delete-form", saveForm);

});
