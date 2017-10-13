'use strict';

$(document).ready(function () {
    console.log('ready from gallery!')
    var socket = new WebSocket("wss://" + window.location.host + "/gallery/");

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