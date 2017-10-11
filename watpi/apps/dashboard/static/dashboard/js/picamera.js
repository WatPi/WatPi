$(function () {
    console.log('$ ready from picamera.js')

    $('.cornerLeft1').on('click', 'a', function (e){
        console.log('this href', $(this).attr('href'));
        $.ajax({
            url: $(this).attr('href'),
            method: 'get',
            success: function (response) {
                console.log('response:', JSON.parse(response))
                let img_url = JSON.parse(response)['image'];
                let img_to_show = "<img src='" + img_url + "'/>";
                console.log(img_to_show);
                $('#photo_frame').append(img_to_show);
            }
        });
    })
    

});