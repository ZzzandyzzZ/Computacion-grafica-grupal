<?php
	$data=$_POST['values'];

	$command = escapeshellcmd('enderezar_imagenSF2.py '.$data);
	echo($command);
	$output = Shell_exec($command);
?>