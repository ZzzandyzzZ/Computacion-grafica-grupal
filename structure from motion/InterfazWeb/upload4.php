<?php
	$data=$_POST['values'];

	$command = escapeshellcmd('enderezar_imagenSF.py '.$data);
	echo($command);
	$output = Shell_exec($command);
?>