$(document).ready(function () {
    $('#suggest-form').on('keyup change paste', ':input', function () {
        var tagText = $('#id_text').val();
        var tagCol = $('#id_colour').val();
        var steamAppId = $('#id_steamAppId').val();
        
        $('#preview-tag').css('background-color', tagCol);
        $('#preview-tag').text(tagText);
        $('#preview-steam').attr('href', "https://store.steampowered.com/app/" + steamAppId);
    });
});