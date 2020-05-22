$(document).ready(function() {
		    $(".upload").on('click', function() {
		        var formData = new FormData();
		        var files = $('#image')[0].files[0];
		        formData.append('file',files);
		        $.ajax({
		            url: 'pru.php',
		            type: 'post',
		            data: formData,
		            contentType: false,
		            processData: false,
		            success: function(response) {
		                if (response != 0) {
		                    $(".card-img-top").attr("src", response);
		                } else {
		                    alert('Formato de imagen incorrecto.');
		                }
		            }
		        });
		        return false;
		    });
		});