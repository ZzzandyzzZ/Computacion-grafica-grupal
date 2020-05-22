var $original,$orgInput,$orgForm;
$(function(){
	$original=$('#original');
	$orgInput=$('#orgInput');
	$orgForm=$('#orgForm');
	$original.on('click',function(){
		$orgInput.click();
	});
	$orgInput.on('change',function(){
		var formData = new FormData();
		formData.append('file',$('#orgInput')[0].files[0]);
		
		$.ajax({
			url:'load_image.php',
			method:'POST',
			data:formData,
			contentType: false,
		    processData: false,
			
		})
		.done(function(data){
			if (data != 0) {
				$("#original").attr("src", data);
			} else {
				alert('Formato de imagen incorrecto.');
			}
		})
		.fail(function(){
			console.log("Fallo");	
		});
	});
	
});