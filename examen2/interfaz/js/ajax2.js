$(document).ready(function() {
    $(".upload2").on('click', function() {
    	let timestamp = Math.floor( Date.now() );
        console.log('exitoooooo')
        var formData = new FormData();
        var files = $('#image2')[0].files[0];
        formData.append('file',files);
        $.ajax({
            url: 'upload2.php',
            type: 'post',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                if (response != 0) {
                    $(".card-img-top").attr("src", response+'?ver='+timestamp);
                    document.getElementById('img2').innerHTML=
                    "<img width=100% src='uploads/suma.jpg?"+Math.random()+"' alt='Nature' class='responsive'>"
                    console.log('exitooooooa')
                } else {
                    alert('Formato de imagen incorrecto.');
                }
            }
        });
        return false;
    });
});