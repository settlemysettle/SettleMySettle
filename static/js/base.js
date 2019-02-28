// when the document is ready, the functions below can be used
$(document).ready(function(){

  // drop login menu down when login button is clicked
  $("#loginButton").click(function() {
    $(".collapse").collapse('show');
  });

  // dynamically change the modal image when clicking on an image
  $(".modalImg").click(function() {
    var src = $(this).attr('src');
    document.getElementById("full-img").src = src;
  });

  // hide login menu when anything but the login button or the box is clicked
  $(document).click(function(e) {
    if ($("#loginDropdownBox").has(e.target).length == 0 && !$("#loginDropdownBox").is(e.target) && !$("#loginButton").is(e.target)) {
      $(".collapse").collapse('hide');
    }
  });

});

