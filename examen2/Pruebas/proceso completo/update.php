<?php
	$data=$_POST['values'];
	
	$command = escapeshellcmd('enderezar_imagen.py '.$data);
	echo($command);
	$output = Shell_exec($command);
?>