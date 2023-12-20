<?php
    $user = "root";
    $pass = ""; 
    $db = "sample";
    $conn = mysqli_connect("localhost", $user, $pass, $db);
    if (!$conn) die("Нет соединения с MySQL");
        
    mysqli_select_db($conn, $db) or die ("Нельзя открыть $db: " . mysqli_error($conn));

    $drop_query = "DROP TABLE IF EXISTS notebook";
    $res = mysqli_query($conn, $drop_query) or die("<p>Error drop: ".mysqli_error());

    $query = "create table notebook(
                id int(4) PRIMARY KEY AUTO_INCREMENT,
                name varchar(50) NOT NULL,
                city  varchar(50) NOT NULL,
                address  varchar(50) NOT NULL,
                birthday  date,
                mail  varchar(20) NOT NULL)";
    $result = mysqli_query($conn, $query) or die ("<p>table cannot created: ".mysql_error());
?>