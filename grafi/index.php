<!DOCTYPE html>
<html>
<head>
	<title>CG</title>
	<link rel="stylesheet" type="text/css" href="estilo.css">
	<script src="https://code.jquery.com/jquery-3.2.1.js"></script>
	<script type="text/php" src="funciones.php"></script>
	<script type="text/javascript" src="refresh.js"></script>
		   
</head>
<body background="fondo2.jpg">
	<h1 style="text-align: center;">Conversor</h1>
  <div>
	<table style="position: relative;right: 0px;top: -15px;">
	
		<tr>
			<td>
				<form enctype="multipart/form-data" action="funciones.php" method="POST">
				    <input type="submit" name="test" id="test" value="Histogram Equalization" /><br/>
				    <input type="submit" name="stretching" id="stretching" value="Contrast Stretching" /><br/>
				    <input type="submit" name="exponencial" id="exponencial" value="Operador exponencial" /><br/>
				    <input type="text" id="e1" name="e1" value="" /><br/>
				    <input type="text" id="e2" name="e2" value="" /><br/>
				    <input type="submit" name="logaritmico" id="logaritmico" value="Operador logarítmico" /><br/>
				    <input type="text" id="log" name="log" value="" /><br/>
				    <input type="submit" name="raiseto" id="raiseto" value="Operador raise to power" /><br/>
				    <input type="text" id="cr" name="cr" value="" /><br/>
				    <input type="text" id="cc" name="cc" value="" /><br/>
				    <input type="submit" name="raiz" id="raiz" value="Operador raíz" />
				    <input type="text" id="ra" name="ra" value="" /><br/>
				    <input type="submit" name="thresholding" id="thresholding" value="Thresholding" />
	    			<input type="text" id="t" name="t" value="" /><br/>
				</form>
			</td>
		</tr>
		


		<tr>
			<td>
				<form enctype="multipart/form-data" action="pru.php" method="POST">
					<input type="file" id="image" name="uploadedfile" /><br/>
					<input type="submit" value="Subir archivo" /><br/>
					<img class="card-img-top" src="uploads/original.jpg ?r=12345" width="200" height="200">
				</form>
				<?php
						clearstatcache();
				?>

				
			</td>
			<td>
				<div>
					<?php
						if(file_exists("uploads/original.jpg")){
							$command = escapeshellcmd('histo.py');
							$output = Shell_exec($command);
							echo '<br/> <br/> <br/> <img src="uploads/histograma.png" width="400" height="200">';
							clearstatcache();
						}
					?>
				</div>
			</td>
			<td>
				<div>
					<?php
						if(file_exists("uploads/resultado.jpg")){
						
							echo '<br/> <br/> <br/><img src="uploads/resultado.jpg ?r=12345" width="200" height="200">';
							clearstatcache();
						}
						
					?>
				</div>
			</td>
		</tr>

	</table>
  </div>
</body>
</html>