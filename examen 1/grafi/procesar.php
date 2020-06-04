<?php
	if($_POST['1']=='1'){
		$command = escapeshellcmd('Histogram_Equalization.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='2'){
		$command = escapeshellcmd('exponencial2.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='3'){
		$command = escapeshellcmd('histo.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='4'){
		$command = escapeshellcmd('logaritmico.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='5'){
		$command = escapeshellcmd('raiseto.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='6'){
		$command = escapeshellcmd('raiz.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='7'){
		$command = escapeshellcmd('Stretching.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='8'){
		$command = escapeshellcmd('Thresholding.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='9'){
		$command = escapeshellcmd('suma.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='10'){
		$command = escapeshellcmd('sumacolor.py');
		$output = Shell_exec($command);
	}

	if($_POST['1']=='11'){
		$command = escapeshellcmd('resta.py');
		$output = Shell_exec($command);
	}

	if($_POST['1']=='12'){
		$command = escapeshellcmd('mult1.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='13'){
		$command = escapeshellcmd('diviescala.py');
		$output = Shell_exec($command);
	}

	if($_POST['1']=='14'){
		$command = escapeshellcmd('divimovi.py');
		$output = Shell_exec($command);
	}
	if($_POST['1']=='15'){
		$command = escapeshellcmd('blending.py');
		$output = Shell_exec($command);
	}