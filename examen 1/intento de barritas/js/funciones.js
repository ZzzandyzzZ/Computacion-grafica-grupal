var dataString = $('form').serialize();
var algorithm;
function proceso(tipo,a,b) {
	console.log(tipo,a,b);
    dataString={"1" : [tipo,a,b]};
	algorithm=tipo;
	$.ajax({
			type: 'POST',
			url: 'procesar.php',
			data: dataString,
			success: function (html) {
					$("#dividR").load(" #dividR");
			}
	});
}
var slider,slider2,a,b;
$(function(){
	slider=$('#slider');
	slider2=$('#slider2');
	slider.on('input',function(){
		proceso(algorithm,this.value,slider2.val());
	});
	slider2.on('input',function(){
		proceso(algorithm,slider.val(),this.value);
	});
	
});