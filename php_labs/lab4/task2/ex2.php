<html> <head>
<title> Task 4.2. add notebook </title> </head> 
<body>

    <?php

        function Add_to_database($name, $city, $address, $birthday, $mail, &$dberror) {
            $user = "root";
            $pass = "";
            $db = "sample";
            $table = "notebook";
            $conn = mysqli_connect("localhost", $user, $pass);
            if (!$conn) {
                $dberror = "Not connected to mysql server";
                return false;
            }
            if (!mysqli_select_db($conn, $db)) {
                $dberror = mysqli_error($conn);
                return false;
            }
            $query = "INSERT INTO $table (name, city, address, birthday, mail) 
                        VALUES('$name', '$city', '$address', '$birthday', '$mail')";
            if (!mysqli_query($conn, $query)) {
                $dberror = mysqli_error($conn);
                mysqli_close($conn);
                return false;
            }
            mysqli_close($conn);
            return true;
        }

        function Write_form() {
            print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
            print "<p>Enter lastname and firstname [*]: <input type='text' name='name'> ";
            print "<p>Enter city: <input type='text' name='city'> ";
            print "<p>Enter address: <input type='text' name='address'> ";
            print "<p>Enter birthday [YYYY-MM-DD]: <input type='text' name='birthday'> ";
            print "<p>Enter e-mail [*]: <input type='text' name='mail'> ";
            print "<p><input type='submit' value='Write!'>\n</form>\n";
            print "<p>Fields marked as [*] are required";
        }

        $PARAMS = (!empty($_POST))? $_POST : $_GET;
        if (!empty($PARAMS['name']) && !empty($PARAMS['mail'])) {
            $dberror = "";
            $name = $PARAMS['name'];
            $city = $PARAMS['city'];
            $address = $PARAMS['address'];
            $birthday = $PARAMS['birthday'];
            $mail = $PARAMS['mail'];

            $ret = Add_to_database($name, $city, $address, $birthday, $mail, $dberror);
            if (!$ret) {
                print "Error: $dberror<br>";
            } else {
                print "Thanks";
            }
        }
        else {
            Write_form();
        }
    ?> 
</body>
</html>