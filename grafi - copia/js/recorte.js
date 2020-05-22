var x1 = 0, y1 = 0, x2 = 0, y2 = 0, anchura = 0, altura = 0;

		$('#mi_imagen').imgAreaSelect({
			fadeSpeed: 300,
			handles: true,
			onSelectEnd: function(img, sel){
				x1 = sel.x1;
				y1 = sel.y1;
				x2 = sel.x2;
				y2 = sel.y2;
				anchura = sel.width;
				altura = sel.height;
			}
		});

		$('#boton_de_recorte').on('click', function(){
			if (anchura == 0 || altura == 0) return;
			$.ajax({
				url:'crear_recorte.php',
				type:'POST',
				data:{
					'x1':x1,
					'y1':y1,
					'x2':x2,
					'y2':y2,
					'anchura':anchura,
					'altura':altura,
					'imagen':'uploads/original.jpg'
				},
				success:function(){
					$('#zona_de_recorte').html('');
					var r = Math.random();
					var recorte = '<img src="uploads/recorte.jpg?' + r + '" alt="" border="0">';
					$('#zona_de_recorte').html(recorte);
					$("#dividR").load(" #dividR");
				}
			});
		});