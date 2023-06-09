var number = 0
var pathInput = '.input-group input'

$(document).ready(function () {
    function checkInputsIsNull() {
        var isNull = false
        $(pathInput).each(function () {
            if ($(this).val().trim() === '') {
                isNull = true
            }
        })
        return isNull
    }

    $('.btn-primary').click(function () {
        if (checkInputsIsNull()) {
            alert("INPUT НЕ МОЖЕТ БЫТЬ ПУСТЫМ!")
        } else {
            number += 1
            var input = $('.input-group').eq(0).clone().show();
            $('.flex-nowrap').before(input);
            $(pathInput).last().attr('name', `input${number}`).val('');
        }
    });
    $('#add').click("submit", function (e) {
        e.preventDefault();
        if (checkInputsIsNull()) {
            alert("INPUT НЕ МОЖЕТ БЫТЬ ПУСТЫМ!")
        } else {
            $("form").submit();
        }
    });
});
