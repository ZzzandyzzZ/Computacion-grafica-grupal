<?php
$target_path = "uploads/";
$target_path = $target_path . basename( $_FILES['uploadedfile']['name']);
if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], "uploads/original.jpg")) {
	header('Location: index.php');
} else{
    echo "Ha ocurrido un error, trate de nuevo!";
}
?>