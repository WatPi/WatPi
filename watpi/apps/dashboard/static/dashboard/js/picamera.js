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
        let img_url = "", img_to_show = "", filename = "", addr = "";
        $.ajax({
            url: $(this).find('a').attr('href'),
            method: 'get',
            success: function (response) {
                parsed_rsp = JSON.parse(response)
                img_url = parsed_rsp['img_url'];
                img_name = parsed_rsp['filename'];
                // addr = parsed_rsp['img_path_to_save'];
                console.log('addr', addr);
                console.log('filename', img_name);
                renderSaveToDrive(img_url, img_name);
                img_to_show = "<img src='/" + img_url + "'/>";
                $('#photo_frame').children().remove();
                $('#photo_frame').append(img_to_show);
            }
        });
    })


});