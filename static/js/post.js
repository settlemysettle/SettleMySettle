$(document).ready(function () {

    console.log("loaded!");
    $('.like_button').on('submit', function (event) {
        event.preventDefault();
        console.log('Trying to like...');

        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            success: function(response) {
                console.log(response);
                $("html").html(response);
            },

            error: function(request, status, error) {
                console.log(request.responseText);
            } 


        });
    });

});