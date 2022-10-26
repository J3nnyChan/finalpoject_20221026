var config={
    width: 180,
    disabled: true,
    icons: {button: "ui-icon-circle-triangle-s"}
    };
  $("#language").selectmenu(config);
  $('#language').on('selectmenuchange', function() {
    var language=$(this).val();
    $("#output").html("最擅長的程式語言是 : " + language);
    });
  $("#open-close").button();
  $("#open-close").on("click", function() {
    var str=$("#open-close").html();
    if (str=="Open") {
      $("#language").selectmenu("open");
      $("#open-close").html("Close");
      }
    else {
      $("#language").selectmenu("close");
      $("#open-close").html("Open");
      }
    });
  $("#enable-disable").button();
  $("#enable-disable").on("click", function() {
    var str=$("#enable-disable").html();
    if (str=="Enable") {
      $("#language").selectmenu("option", "disabled", false);
      //$("#language").selectmenu("enable");  //另一個做法
      $("#enable-disable").html("Disable");
      }
    else {
      $("#language").selectmenu("disable");
      $("#enable-disable").html("Enable");
      }
    });