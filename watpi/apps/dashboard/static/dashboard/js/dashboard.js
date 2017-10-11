$(function () {
    console.log('$ ready!')

    $('.cornerRight1, .cornerRight2, .cornerLeft1, .cornerLeft2, #forward, #backward, #left, #right').hover(
        function () {
            $(this).addClass('animated pulse');
        }, function () {
            $(this).removeClass('animated pulse');
        }
    )

});