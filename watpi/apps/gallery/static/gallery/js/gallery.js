'use strict';

$(document).ready(function () {
    console.log('ready from gallery!')
    var socket = new WebSocket("ws://" + window.location.host + "/gallery/");

    // $('#trigger').click(function (event) {
    //     event.preventDefault();
    //     // var img = getBase64Image($('#store')[0]);
    //     var sendIt = JSON.stringify({
    //         "text": {
    //             "imgnum": 1,
    //             // "image": img,
    //         }
    //     });
    //     socket.send(sendIt);
    // });

    socket.onmessage = function (event) {
        console.log('i am here')
        var text = JSON.parse(event.data);
        console.log(text)
        if (text) {
            var img = $('<img />').attr('src', 'data:image/png;base64,' + text.image).attr('height', '200');
            $('#emit').html(img);
        }
    }
})