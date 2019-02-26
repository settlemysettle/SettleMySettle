$(document).ready(function(){

  $("#loginButton").click(function(){
    $(".collapse").collapse('show');
  });

  $(document).click(function(e){
    if ($("#loginDropdown").has(e.target).length == 0 && !$("#loginDropdown").is(e.target) && !$("#loginButton").is(e.target)) {
      $(".collapse").collapse('hide');
    }
  });

});