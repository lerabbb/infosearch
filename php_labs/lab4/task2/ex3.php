<html> <head>
<title> Task 4.3. read notebook </title>
</head> <body>

    <?php
        $user = "root";
        $pass = "";
        $db = "sample";
        $table = "notebook";
        $conn = mysqli_connect("localhost", $user, $pass);
        if (!$conn) die("Нет соединения с MySQL");
        mysqli_select_db($conn, $db) or die ("Нельзя открыть $db: " .mysqli_error($conn));
        
        $result = mysqli_query($conn, "SELECT * FROM $table");
        $num_rows = mysqli_num_rows($result);
        $num_fields = mysqli_num_fields($result);
        
        print "<table border=1 cellpadding=5>\n";
        print "<tr>";
        for ($x = 0; $x < $num_fields; $x++) {
            $name = mysqli_fetch_field_direct($result, $x)->name;
            $transl = $rus_name[$name];
            print "\t<th>$transl<br>$name</br></th>";
        }
        print "</tr>\n";

        while ($a_row = mysqli_fetch_row($result)) {
            print "<tr>";
            foreach ($a_row as $field)
                print "\t<td>$field</td>";
            print "</tr>\n";
        }
        print "</table>\n";
    ?>
</body>
</html>