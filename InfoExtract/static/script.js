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
    $(".toggle-text").click(function (e) {
        e.preventDefault();
        var textDiv = $(this).prev(".chunk-text").find(".short-text, .full-text");
        var currentState = $(this).data("state");
        if (currentState === "short") {
            textDiv.hide();
            $(this).data("state", "full").text("Show More");
        } else {
            textDiv.show();
            $(this).data("state", "short").text("Show Less");
        }
        var $chunkText = $(this).closest(".chunk-text");
        $chunkText.find(".short-text").toggle();
        $chunkText.find(".full-text").toggle();
        return false;
    });
});