$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-subledger .modal-content").html("");
          $("#modal-subledger").modal("show");
        },
        success: function (data) {
          $("#modal-subledger .modal-content").html(data.html_form);
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
            $("#subledger-table tbody").html(data.html_subledger_list);
            $("#modal-subledger").modal("hide");
          }
          else {
            $("#modal-subledger .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create subledger
    $(".js-create-subledger").click(loadForm);
    $("#modal-subledger").on("submit", ".js-subledger-create-form", saveForm);
  
    // Update subledger
    $("#subledger-table").on("click", ".js-update-subledger", loadForm);
    $("#modal-subledger").on("submit", ".js-subledger-update-form", saveForm);
  
    // Delete subledger
    $("#subledger-table").on("click", ".js-delete-subledger", loadForm);
    $("#modal-subledger").on("submit", newFunction(), saveForm);
  
  });

function newFunction() {
    return ".js-subledger-delete-form";
}
  