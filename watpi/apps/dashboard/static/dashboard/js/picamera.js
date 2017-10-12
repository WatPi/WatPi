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

    // initiate WebSocket
    var socket = new WebSocket("ws://" + window.location.host + "/dashboard/");

    $('#take_photo').on('click', function (e){
        event.preventDefault();
        
        // send websocket signal
        var sendIt = JSON.stringify({
            "text": {
                "imgnum": 1,
            }
        });
        socket.send(sendIt);
        
        let img_url = "", img_to_show = "", filename = "", addr = "";
        $.ajax({
            url: $(this).find('a').attr('href'),
            method: 'get',
            success: function (response) {
                parsed_rsp = JSON.parse(response)
                img_url = parsed_rsp['img_url'];
                img_name = parsed_rsp['filename'];
                // #Google Drive
                addr = "../static/dashboard/images/" + img_name;
                renderSaveToDrive(addr, img_name);
                img_to_show = "<img src='/" + img_url + "'/>";
                $('#photo_frame').children().remove();
                $('#photo_frame').append(img_to_show);
            }
        });
    })

});