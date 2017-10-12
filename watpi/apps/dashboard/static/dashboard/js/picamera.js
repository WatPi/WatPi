// ++++++++++ Google Drive +++++++++
function renderSaveToDrive(src, filename) {
    gapi.savetodrive.render('savetodrive-div', {
        src: src,
        filename: filename,
        sitename: 'WatPi'
    });
}

$(function () {
    console.log('$ ready from picamera.js')

    $('#take_photo').on('click', function (e){
        let img_url = "", img_to_show = "", filename = "";
        $.ajax({
            url: $(this).find('a').attr('href'),
            method: 'get',
            success: function (response) {
                img_url = JSON.parse(response)['image_path'];
                img_name = JSON.parse(response)['filename'];
                console.log('url', img_url)
                console.log('filename', img_name)
                renderSaveToDrive(img_url, img_name)
                img_to_show = "<img src='/" + img_url + "'/>";
                $('#photo_frame').children().remove();
                $('#photo_frame').append(img_to_show);
            }
        });
    })


});