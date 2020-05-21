<!DOCTYPE html>
<html>
<head>
	<title>CG</title>
	<link rel="stylesheet" type="text/css" href="estilo.css">
	<script src="https://code.jquery.com/jquery-3.2.1.js"></script>
	<script type="text/javascript">
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
	</script>
</head>
<body background="fondo2.jpg">
	<h1 style="text-align: center;">Conversor</h1>
  <div>
	<table style="position: relative;right: 0px;top: -15px;">
	
		<tr>
			<td>
				<form method="post">
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
			if( isset($_POST['log']) )
			{
			    $l = $_POST['log'];
			}
			$command = escapeshellcmd('logaritmico.py '.$l);
			$output = Shell_exec($command);
		}
		if(array_key_exists('logaritmico',$_POST)){
		   logaritmico();
		}
		function exponencial()
		{
			if( isset($_POST['e1']) )
			{
			    $ex1 = $_POST['e1'];
			}
			if( isset($_POST['e2']) )
			{
			    $ex2 = $_POST['e2'];
			}
			$command = escapeshellcmd('exponencial2.py '.$ex1.' '.$ex2);
			$output = Shell_exec($command);
		}
		if(array_key_exists('exponencial',$_POST)){
		   exponencial();
		}
		function raiseto()
		{
			if( isset($_POST['cr']) )
			{
			    $raise1 = $_POST['cr'];
			}
			if( isset($_POST['cc']) )
			{
			    $raise2 = $_POST['cc'];
			}
			$command = escapeshellcmd('raiseto.py '.$raise1.' '.$raise2);
			$output = Shell_exec($command);
		}
		if(array_key_exists('raiseto',$_POST)){
		   raiseto();
		}
		function raiz()
		{
			if( isset($_POST['ra']) )
			{
			    $r = $_POST['ra'];
			}
			$command = escapeshellcmd('raiz.py '.$r);
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