$(document).ready(function () {
    $('#suggest-form').on('keyup change paste', ':input', function () {
        console.log("inputs change!");

        var tagText = $('#id_text').val();
        var tagCol = $('#id_colour').val();

        console.log(tagText + ", " + tagCol);

        $('#preview-tag').css('background-color', tagCol);
        $('#preview-tag').text(tagText);
    });
});