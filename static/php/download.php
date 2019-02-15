<?php
//got file
$file = $_GET['file'];
//told php that it is an png
header('Content-type: image/png');
//told php that it is an attachment
header("Content-disposition: attachment; filename=canvasoutput.png");
//spit out file
readfile($file);

?>