<?php
		function puntos()
		{

			$command = escapeshellcmd('puntos.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('puntos',$_POST)){
		   header('Location: index.php');
		   puntos();
		}