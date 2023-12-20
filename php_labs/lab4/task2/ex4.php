<html> <head>
<title> Task 4.4. Update notebook
</title> </head> <body>

    <?php
        function vid_content($conn, $table) {
            $result = mysqli_query($conn, "SELECT * FROM $table");
            $num_rows = mysqli_num_rows($result);
            $num_fields = mysqli_num_fields($result);
            print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
            print "<table border=1 cellpadding=5>\n";
            print "<tr>";
            for ($x = 0; $x < $num_fields; $x++) {
                $name = mysqli_fetch_field_direct($result, $x)->name;
                $transl = $rus_name[$name];
                print "\t<th>$transl<br>$name</br></th>";
            }
            print "\t<th>update</th>";
            print "</tr>\n";
            while ($a_row = mysqli_fetch_row($result)) {
                print "<tr>";
                foreach ($a_row as $field)
                    print "\t<td>$field</td>";
                print "\t<td><input type=\"radio\" name=\"id\" value=\"$a_row[0]\"></td>\n";
                print "</tr>\n";
            }
            print "</table>\n";
            print "<p><input type='submit' value='Choose'>\n</form>\n";
        }
  
        $user = "root";
        $pass = "";
        $db = "sample";
        $table = "notebook";
        $conn = mysqli_connect("localhost", $user, $pass);
        if (!$conn) die("Нет соединения с MySQL");
        mysqli_select_db($conn, $db) or die ("Нельзя открыть $db");
        vid_content($conn, $table);
    
        if (isset($_POST['id'])) {
            $id = $_POST['id'];
            if(isset($_POST['field_name'])){
                $field_name = $_POST['field_name'];
                $field_value = $_POST['field_value'];
                $query = "UPDATE $table SET $field_name='$field_value' WHERE id='$id'";
                $result = mysqli_query($conn, $query);
                if (!$result) die ("Cannot update: " . mysqli_error($conn));
                print"<p>Table $table updated: ". mysqli_affected_rows($conn) . " lines changed\n";
                print "<a href=\"ex3.php\">Go to table</a>";
                mysqli_close($conn);
            } else {
                print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
                print "<select name='field_name'>";
                $result = mysqli_query($conn, "SELECT * FROM $table WHERE id=$id");
                $a_row = mysqli_fetch_array($result);
                $num_fields = mysqli_num_fields($result);
                for ($x = 0; $x < $num_fields; $x++) {
                    $name = mysqli_fetch_field_direct($result, $x)->name;
                    print "<option value='$name'>$a_row[$x]\n";
                }
                mysqli_close($conn);
                print "</select> &nbsp;&nbsp;Enter new value: <input type='text' name='field_value'></p>";
                print "<input type='hidden' name='id' value=$id>";
                print "<p><input type='submit' value='Update'>";
                print "</form>";
            }
        }
    ?>
    </form>
</body>
</html>