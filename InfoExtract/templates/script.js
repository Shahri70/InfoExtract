$(document).ready(function () {
    // Submit form using AJAX to avoid page refresh
    $("#filter-form").submit(function (e) {
        e.preventDefault();
        var selectedTopic = $("#selected_topic").val();
        $.post("/filter", { selected_topic: selectedTopic }, function (data) {
            $("#filtered_data").html(data);
        });
    });

    // Toggle full text
    $(".toggle-text").click(function () {
        var $chunkText = $(this).closest(".chunk-text");
        $chunkText.find(".short-text").toggle();
        $chunkText.find(".full-text").toggle();
        return false;
    });
});