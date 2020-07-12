<?php
	$data=$_POST['values'];
	
	$command = escapeshellcmd('python3 enderezar_imagen.py '.$data);
	echo($command);
	$output = Shell_exec($command);
?>