$(document).ready(function() {
    $(".upload2").on('click', function() {
        let timestamp = Math.floor( Date.now() );
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
                 $("#divid").load(" #divid");
                } else {
                    alert('Formato de imagen incorrecto.');
                }
            }

        });
        return false;
    });


    
    
});