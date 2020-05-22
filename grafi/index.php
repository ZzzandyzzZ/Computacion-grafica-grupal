<!DOCTYPE html>
<html>
<head>
	<title>CG</title>
	<script type="text/javascript" src="js/jquery-3.5.1.min.js"></script>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/ajax.js"></script>
	<script type="text/javascript" src="js/funciones.js"></script>
	<meta charset="utf-8">

</head>
<body>
	<div class="container">
	<nav class="navbar navbar-dark bg-dark">
		<form class="form-inline" onsubmit="return false" name="formularioUsuario">
    		<button class="btn btn-outline-success" type="button" onclick="proceso(1)">Histogram</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(2)">Op. Exponencial</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(4)">Op. Logaritmico</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(5)">Op. raiz</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(7)">Contrast Stretching</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(8)">Thresholding</button>

		</form>
	</nav>

	<form enctype="multipart/form-data" action="#" method="POST">
	<div class="input-group mb-3">
		<div class="input-group-prepend">
			<button class="btn btn-outline-secondary upload" type="submit" onclick="proceso(3)">Subir</button>
		</div>
		<div class="custom-file">
			<input type="file" class="custom-file-input" id="image" name="image">
			<label class="custom-file-label" for="image">Escoga un archivo</label>
		</div>
	</div>
	</form>
	</div>
	<div class="container">
		<div class="row align-items-center">
			<div id="divid" name="divid">
				<?php
					if(file_exists("uploads/original.jpg")){

						$direc = '<img src="uploads/original.jpg?'.rand().'" class="img-fluid" alt="Responsive image">';
						$direc2 = '<img align="right" src="uploads/histograma.png?'.rand().'" class="img-fluid" alt="Responsive image">';
					echo $direc.$direc2;
					}
				?>
			</div>
			<div id="dividR" name="dividR">
				<?php
					if(file_exists("uploads/resultado.jpg")){
						$direc = '<img src="uploads/resultado.jpg?'.rand().'" class="img-fluid" alt="Responsive image">';
					echo $direc;
					}
				?>
			</div>
		</div>
	</div>
</body>
</html>