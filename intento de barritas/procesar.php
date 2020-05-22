<?php
	
	
	if($_POST['1'][0]=='1'){
		$command = escapeshellcmd('Histogram_Equalization.py '.);
		$output = Shell_exec($command);
		
	}
	if($_POST['1'][0]=='2'){
		$command = escapeshellcmd('exponencial2.py');
		$output = Shell_exec($command);
	}
	if($_POST['1'][0]=='3'){
		$command = escapeshellcmd('histo.py');
		$output = Shell_exec($command);
	}
	if($_POST['1'][0]=='4'){
		$command = escapeshellcmd('logaritmico.py');
		$output = Shell_exec($command);
	}
	if($_POST['1'][0]=='5'){
		$command = escapeshellcmd('raiseto.py');
		$output = Shell_exec($command);
	}
	if($_POST['1'][0]=='6'){
		$command = escapeshellcmd('raiz.py');
		$output = Shell_exec($command);
	}
	if($_POST['1'][0]=='7'){
		$command = escapeshellcmd('Stretching.py');
		$output = Shell_exec($command);
	}
	if($_POST['1'][0]=='8'){
		echo "<script>console.log('Debug Objects:' );</script>";
		$command = escapeshellcmd('python3 Thresholding.py '.$_POST['1'][1].' '.$_POST['1'][2]);
		$output = Shell_exec($command);
	}