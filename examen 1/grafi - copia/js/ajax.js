$(document).ready(function() {
    $(".upload").on('click', function() {
    	let timestamp = Math.floor( Date.now() );
        var formData = new FormData();
        var files = $('#image')[0].files[0];
        formData.append('file',files);
        $.ajax({
            url: 'upload.php',
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