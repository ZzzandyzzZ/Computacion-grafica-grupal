<!DOCTYPE html>
<html>
<head>
	<title>CG</title>
	<link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body background="fondo2.jpg">
	<h1 style="text-align: center;">Conversor</h1>
  <div>
	<table style="position: relative;left: 380px;top: 50px;">
		<tr>
			<td>
				<form enctype="multipart/form-data" action="pru.php" method="POST">
			</td>
			<td>
				<input name="uploadedfile" type="file" />

				<input type="submit" value="Subir archivo" />

			</form>
		</tr>
		<tr>
			<td>
				<form method="post">
				    <input type="submit" name="test" id="test" value="Histogram Equalization" /><br/>
				    <input type="submit" name="stretching" id="stretching" value="Contrast Stretching" /><br/>
				    <input type="submit" name="exponencial" id="exponencial" value="Operador exponencial" /><br/>
				    <input type="submit" name="logaritmico" id="logaritmico" value="Operador logarítmico" /><br/>
				    <input type="submit" name="raiseto" id="raiseto" value="Operador raise to power" /><br/>
				    <input type="submit" name="raiz" id="raiz" value="Operador raíz" /><br/>
				    <input type="submit" name="thresholding" id="thresholding" value="Thresholding" />
	    			<input type="text" id="t" name="t" value="" /><br/>
				</form>
			</td>
		</tr>
		<tr>
			<td>
				<div>
					<?php
						if(file_exists("uploads/original.jpg")){
							echo '<img src="uploads/original.jpg">';
						}
					?>
				</div>
			</td>


	<?php
		function testfun()
		{
			$command = escapeshellcmd('Histogram_Equalization.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('test',$_POST)){
		   testfun();
		}
		function contrastStretching()
		{
			$command = escapeshellcmd('Stretching.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('stretching',$_POST)){
		   contrastStretching();
		}
		function logaritmico()
		{
			$command = escapeshellcmd('logaritmico.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('logaritmico',$_POST)){
		   logaritmico();
		}
		function exponencial()
		{
			$command = escapeshellcmd('exponencial2.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('exponencial',$_POST)){
		   exponencial();
		}
		function raiseto()
		{
			$command = escapeshellcmd('raiseto.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('raiseto',$_POST)){
		   raiseto();
		}
		function raiz()
		{
			$command = escapeshellcmd('raiz.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('raiz',$_POST)){
		   raiz();
		}
		function thresholding()
		{

			if( isset($_POST['t']) )
			{
			    $tr = $_POST['t'];
			}
			$command = escapeshellcmd('Thresholding.py '.$tr);
			$output = Shell_exec($command);
		}
		if(array_key_exists('thresholding',$_POST)){
		   thresholding();
		}
	?>
			<td>
				<div>
					<?php
						if(file_exists("uploads/original.jpg")){
							$command = escapeshellcmd('histo.py');
							$output = Shell_exec($command);
							echo '<img src="uploads/histograma.png" width="500" height="300">';
						}
					?>
				</div>
			</td>
			<td>
				<div>
					<?php
						if(file_exists("uploads/resultado.jpg")){
							echo '<img src="uploads/resultado.jpg">';
						}
					?>
				</div>
			</td>
	</tr>
	</table>
  </div>
</body>
</html>