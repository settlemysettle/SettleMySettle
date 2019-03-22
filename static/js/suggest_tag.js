$(document).ready(function () {

    // updates tag dynamically
    $.fn.updatePreview = function() {
        var tagText = $('#exampleFormControlTextarea1').val();
        var tagCol = $('#cPicker').val();
        var steamAppId = $('#sAppID').val();
        
        $('#preview-tag').css('background-color', tagCol);
        $('#preview-tag').text(tagText);
        $('#preview-steam').attr('href', "https://store.steampowered.com/app/" + steamAppId);
    }
    $('#suggest-form').on('keyup change paste', ':input', function () {
        $.fn.updatePreview();
    });

    // places the tag information into the form to be modified/approved
    $('.edit-tag').click( function() {
        
        var tagInfo = $(this).closest('tr').children('td') // get list of items in this row
        var tagColText = tagInfo.get(0).id;

        var tagCol = tagColText.substring(0, 7);
        var tagText = tagColText.substring(7, );

        var tagSteamAppId = tagInfo.get(1).id;

        var tagIsGame = tagInfo.get(3).id;

        $('#exampleFormControlTextarea1').val(tagText);
        $('#cPicker').val(tagCol);
        $('#sAppID').val(tagSteamAppId);
        $('#gTag').prop('checked', tagIsGame === "True");

        $.fn.updatePreview();
    });

    
});