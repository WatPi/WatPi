$(function () {
    console.log('$ ready from picamera.js')

    $('#take_photo').on('click', function (e){
        let img_url = "", img_to_show = "";
        $.ajax({
            url: $(this).find('a').attr('href'),
            method: 'get',
            success: function (response) {
                img_url = JSON.parse(response)['image'];
                img_to_show = "<img src='/" + img_url + "'/>";
                $('#photo_frame').children().remove();
                $('#photo_frame').append(img_to_show);
            }
        });
    })

});