$(document).ready(function () {
    $('#suggest-form').on('keyup change paste', ':input', function () {
        var tagText = $('#id_text').val();
        var tagCol = $('#id_colour').val();
        var steamAppId = $('#id_steamAppId').val();
        
        $('#preview-tag').css('background-color', tagCol);
        $('#preview-tag').text(tagText);
        $('#preview-steam').attr('href', "https://store.steampowered.com/app/" + steamAppId);
    });

    $('.edit-tag').click( function() {
        console.log("editing required?");
        var tagInfo = $(this).closest('tr').attr('id');
        console.log(tagInfo);

        var tagCol = tagInfo.substring(0, 7);
        var tagText = tagInfo.substring(7, );

        console.log(tagCol);
        console.log(tagText);

        $('#id_text').val(tagText);
        $('#id_colour').val(tagCol);


    });

    
});