$(document).ready(function () {

    $.fn.updatePreview = function() {
        var tagText = $('#id_text').val();
        var tagCol = $('#id_colour').val();
        var steamAppId = $('#id_steamAppId').val();
        
        $('#preview-tag').css('background-color', tagCol);
        $('#preview-tag').text(tagText);
        $('#preview-steam').attr('href', "https://store.steampowered.com/app/" + steamAppId);
    }
    $('#suggest-form').on('keyup change paste', ':input', function () {
        $.fn.updatePreview();
    });

    $('.edit-tag').click( function() {
        
        console.log("editing required?");
        var tagInfo = $(this).closest('tr').children('td') // get list of items in this row
        console.log(tagInfo);
        var tagColText = tagInfo.get(0).id;

        var tagCol = tagColText.substring(0, 7);
        var tagText = tagColText.substring(7, );

        var tagSteamAppId = tagInfo.get(1).id;

        var tagIsGame = tagInfo.get(2).id;

        $('#id_text').val(tagText);
        $('#id_colour').val(tagCol);
        $('#id_steamAppId').val(tagSteamAppId);
        $('#id_is_game_tag').prop('checked', tagIsGame === "True");

        $.fn.updatePreview();
    });

    
});