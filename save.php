<?php
$data = $_POST['img'];

$data = str_replace('data:image/png;base64,', '', $data);
$data = str_replace(' ', '+', $data);

$img = base64_decode($data);
$path = 'images/' . uniqid() . '.png';
// $image = imagecreatefrompng('C:\Users\Rajul Manandhar\Downloads\canvasoutput.png');
// $colors = explode(',', '255,255,255');
// $remove = imagecolorallocate($image,255,255,255);
// imagecolortransparent($image, $remove);
// imagepng($image, 'C:\xampp\htdocs\HelloWorld\request.png');
if(file_put_contents($path, $img))
{
    print $path;
}
else
{
    header("HTTP/1.1 500 Internal Server Error");
}
cropImage(32,32,$path,'png','images/request.png');



function cropImage($nw, $nh, $source, $stype, $dest) {
    $size = getimagesize($source);
    $w = $size[0];
     $h = $size[1];

     switch($stype) {
         case 'gif':
         $simg = imagecreatefromgif($source);
         break;
         case 'jpg':
         $simg = imagecreatefromjpeg($source);
         break;
         case 'png':
         $simg = imagecreatefrompng($source);
         break;
     }

     $dimg = imagecreatetruecolor($nw, $nh);
     // start changes
    switch ($stype) {
    case 'gif':
    case 'png':
        // integer representation of the color black (rgb: 0,0,0)
        $background = imagecolorallocate($dimg , 0, 0, 0);
        // removing the black from the placeholder
        imagecolortransparent($dimg, $background);

        // turning off alpha blending (to ensure alpha channel information
        // is preserved, rather than removed (blending with the rest of the
        // image in the form of black))
        imagealphablending($dimg, false);

        // turning on alpha channel information saving (to ensure the full range
        // of transparency is preserved)
        imagesavealpha($dimg, true);
        break;

    default:
        break;
}
// end changes

     $wm = $w/$nw;
     $hm = $h/$nh;
     $h_height = $nh/2;
     $w_height = $nw/2;

     if($w> $h) {
         $adjusted_width = $w / $hm;
         $half_width = $adjusted_width / 2;
         $int_width = $half_width - $w_height;
         imagecopyresampled($dimg,$simg,-$int_width,0,0,0,$adjusted_width,$nh,$w,$h);
     } elseif(($w <$h) || ($w == $h)) {
         $adjusted_height = $h / $wm;
         $half_height = $adjusted_height / 2;
         $int_height = $half_height - $h_height;

         imagecopyresampled($dimg,$simg,0,-$int_height,0,0,$nw,$adjusted_height,$w,$h);
     } else {
         imagecopyresampled($dimg,$simg,0,0,0,0,$nw,$nh,$w,$h);
     }

     imagejpeg($dimg,$dest,100);
}
?>