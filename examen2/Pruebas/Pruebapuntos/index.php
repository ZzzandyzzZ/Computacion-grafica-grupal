<!DOCTYPE html>
<html>
<head>
	<title>Coordenadas</title>
</head>
<body>
<div>
	<form enctype="multipart/form-data" action="pru.php" method="POST">
		<input name="uploadedfile" type="file" />
		<input type="submit" value="Subir archivo" />	
	</form>
</div>
<div>
	<form action="funcion.php" method="POST">
		<input type="submit" name="puntos" id="puntos" value="puntos" /><br/>		   
	</form>
</div>
<div>
	<?php
		if(file_exists("uploads/original.jpg")){
			echo '<img src="uploads/original.jpg">';
		}
	?>
</div>
<div>
	<?php
		if(file_exists("uploads/resultado.jpg")){
			echo '<br/> <br/> <br/><img src="uploads/resultado.jpg ?r=12345" width="200" height="200">';
		}
	?>
</div>
<div>
	<?php
			$archivo = fopen("puntos.txt", "r");
			$iterator=0;
			while(!feof($archivo)){
				$traer = fgets($archivo);
				$iterator++;
				if($iterator==1)
				{
					$cord=$traer;
				}
		    }
		    echo nl2br($cord);
			fclose($archivo);

	?>
	<script type="text/javascript">
   		 var cord = '<?php echo $cord;?>';
   		 var coordenadas = cord.split(',');
   		 var px1 = parseInt(coordenadas[0]);
   		 var py1 = parseInt(coordenadas[1]);
   		 var px2 = parseInt(coordenadas[2]);
   		 var py2 = parseInt(coordenadas[3]);
   		 var px3 = parseInt(coordenadas[4]);
   		 var py3 = parseInt(coordenadas[5]);
   		 var px4 = parseInt(coordenadas[6]);
   		 var py4 = parseInt(coordenadas[7]);
   		 console.log(px1);
	</script>
</div>
</body>
</html>