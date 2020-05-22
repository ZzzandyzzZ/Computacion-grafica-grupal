<?php
if (($_FILES["file"]["type"] == "image/pjpeg")
    || ($_FILES["file"]["type"] == "image/jpeg")
    || ($_FILES["file"]["type"] == "image/png")
    || ($_FILES["file"]["type"] == "image/gif")) {
    if (move_uploaded_file($_FILES["file"]["tmp_name"], "uploads/original.jpg")) {
        //more code here...
        echo "uploads/".$_FILES['file']['name'];
    } else {
        echo 0;
    }
} else {
    echo 0;
}
