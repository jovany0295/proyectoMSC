<?php

    header('Access-Control-Allow-Origin: *');
    $mac = $_GET["dato"];

    $conectar= mysqli_connect("localhost","sistemas","Aca$","ricsa") or die ("no se pudo realizar la conexion");

    if (!$conectar) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $resultA=mysqli_query($conectar,"SELECT * FROM login WHERE ap like '%anclas%'");
    $anclas=mysqli_num_rows($resultA);
    $resultC=mysqli_query($conectar,"SELECT * FROM login WHERE ap like '%cine%'");
    $cinerio=mysqli_num_rows($resultC);
    $resultE=mysqli_query($conectar,"SELECT * FROM login WHERE ap like '%emotion%'");
    $emotion=mysqli_num_rows($resultE);
    
   
   
    echo $anclas+',',$cinerio+',',$emotion;
    
   
?>