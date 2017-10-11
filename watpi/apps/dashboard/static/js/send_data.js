function getBase64Image(img) {
    // Create an empty canvas element
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;

    // Copy the image contents to the canvas
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);

    // Get the data-URL formatted image
    // Firefox supports PNG and JPEG. You could check img.src to guess the
    // original format, but be aware the using "image/jpg" will re-encode the image.
    var dataURL = canvas.toDataURL("image/png");

    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}

$(document).ready(function() {
  var socket = new WebSocket("ws://" + window.location.host + "/dashboard/");
  $('#left-side').click(function(event) {
    event.preventDefault();
    var src1 = '/static/images/dashboard/group_selfie.jpg';
    var src2 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
    var imgtag = '<img src="' + src1 + '>"';
    // $imgsrc = $('<img />').attr('src', src2)
    // $(imgtag).on('load',  function() {
    // });
    // console.log(this)
    // console.log($(this))
    var img = getBase64Image($('#store')[0]);
    console.log($('#store'))
    // var img = "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
    var sendIt = JSON.stringify({
      "text": {
        "image": img,
      }
    });
    socket.send(sendIt);
    // imgtag.attr('height', 200);
  });
  socket.onmessage = function(event) {
    var text = JSON.parse(event.data).text;
    if(text){
      var src = "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==";
      var img = $('<img />').attr('src', 'data:image/png;base64,' + text.image);
      console.log(text);
      // var outText = "<p>You emitted the following information to the server: ";
      // outText += "</p>";
      // console.log(out);
      // outText += JSON.stringify(out) + "</p>";
    }
    $('#emit').append(img);
  }
})
