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
    // var filename = '../images/dashboard/group_selfie.jpg';
    // var img = $('<img />').attr('src', '../images/dashboard/group_selfie.jpg');
    // var img = "nothing here";
    var img = getBase64Image($('#grpslf'));
    // img = fetch($('#grpslf'))
    //   .then(function(response){
    //     return response.blob();
    //   })
    console.log(img);
    var sendIt = JSON.stringify({
      "text": {
        "image": img,
      }
    });
    socket.send(sendIt);
  });
  socket.onmessage = function(event) {
    var text = JSON.parse(event.data).text;
    if(text){
      var out = {
        "image": text.image,
      }
      var outText = "<p>You emitted the following information to the server: ";
      outText += "</p>";
      console.log(out);
      // outText += JSON.stringify(out) + "</p>";
    }
    $('#emit').html(outText);
  }
})
