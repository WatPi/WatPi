$(function () {
    console.log("$ ready!");

    $('#rover').on('vmousedown', function(e){
        let direction = e.target.id, 
            data_to_django = JSON.stringify({'direction': direction}); 
        console.log('url', $(this).find('a').attr('href'));
        console.log('data', data_to_django);
        $.ajax({
            url: $(this).find('a').attr('href'),
            method: 'get',
            data: data_to_django,
            success: function (response) {
                console.log('response:', JSON.parse(response))
            }
        });
    })

    $('#rover').on('vmouseup', function(e){
        console.log('vmouseup, stop')
    })

});