<?php
	$data=$_POST['values'];
	echo($data);
	$command = escapeshellcmd('');
	$output = Shell_exec($command);
?>