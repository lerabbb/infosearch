<html> <head>
<title> Task 4.5. add notebook </title> </head> 
<body>

<?php
    function connect(){
        $user = "root";
        $pass = "";
        $db = "sample";
        $table = "notebook";
        $conn = mysqli_connect("localhost", $user, $pass);
        if (!$conn) {
            $dberror = "Not connected to mysql server";
        }
        if (!mysqli_select_db($conn, $db)) {
            $dberror = mysqli_error($conn);
        }
        return $conn;
    }

    function Add_to_database($conn, $name, $city, $address, $birthday, $mail) {
        
        $query = "INSERT INTO $table (name, city, address, birthday, mail) 
                    VALUES('$name', '$city', '$address', '$birthday', '$mail')";
        if (!mysqli_query($conn, $query)) {
            $dberror = mysqli_error($conn);
        }
    }
    
    $conn = connect();
    Add_to_database($conn, 'Ivanov Ivan', 'Novosibirsk', 'Pirogova, 16', '2000-12-21', 'ivan@mail.ru');
    Add_to_database($conn, 'Petrov Petr', 'Novosibirsk', 'Morskoy prospekt. 20', '1956-', 'petr@mail.ru');
    Add_to_database($conn, 'Pavlov Pavel', 'Moscow', 'Lenina', '1990-04-20', 'pavel@mail.ru');
    mysqli_close($conn);
?>
</body> </html>