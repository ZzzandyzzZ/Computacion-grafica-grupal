<?php
		function testfun()
		{
			$command = escapeshellcmd('Histogram_Equalization.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('test',$_POST)){
		   header('Location: index.php');
		   testfun();

		}
		function contrastStretching()
		{
			$command = escapeshellcmd('Stretching.py');
			$output = Shell_exec($command);
		}
		if(array_key_exists('stretching',$_POST)){
			header('Location: index.php');
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
		   header('Location: index.php');
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
		   header('Location: index.php');
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
		   header('Location: index.php');
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
		   header('Location: index.php');
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
		   header('Location: index.php');
		   thresholding();
		}
	?>