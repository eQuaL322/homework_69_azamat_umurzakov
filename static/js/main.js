$(document).ready(function () {
    function sendRequest(operation) {
        let num1 = parseFloat($("#number-a").val());
        let num2 = parseFloat($("#number-b").val());

        if (isNaN(num1) || isNaN(num2)) {
            $("#result")
                .text("Invalid input.")
                .css("color", "red");
            return;
        }

        $.ajax({
            type: "POST",
            url: "/" + operation + "/",
            contentType: "application/json",
            data: JSON.stringify({A: num1, B: num2}),
            success: function (response) {
                $("#result")
                    .text("Result: " + response.answer)
                    .css("color", "green");
            },
            error: function (xhr) {
                let errorMessage = xhr.responseJSON.error;
                $("#result")
                    .text("Error: " + errorMessage)
                    .css("color", "red");
            }
        });
    }

    $("#add").click(function () {
        sendRequest("add");
    });

    $("#subtract").click(function () {
        sendRequest("subtract");
    });

    $("#multiply").click(function () {
        sendRequest("multiply");
    });

    $("#divide").click(function () {
        sendRequest("divide");
    });
});
