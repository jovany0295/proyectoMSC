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
    $resultV=mysqli_query($conectar,"SELECT * FROM login WHERE ap like '%vegas%'");
    $vegas=mysqli_num_rows($resultV);
    $resultP=mysqli_query($conectar,"SELECT * FROM login WHERE ap like '%pueblito%'");
    $pueblito=mysqli_num_rows($resultP);
    $resultU=mysqli_query($conectar,"SELECT * FROM login WHERE ap like '%UPN%'");
    $UPN=mysqli_num_rows($resultU);
    
   
   
    echo $anclas.',',$cinerio.',',$emotion.',',$vegas.',',$pueblito;
    
   
?>