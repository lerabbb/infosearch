<?php
    $list_sites = array(
        "www.yandex.ru",
        "www.rambler.ru",
        "www.google.com",
        "www.yahoo.com",
        "www.altavista.com"
    ); 

    if (isset ($_POST["site"])) {
        $site = $_POST["site"];
        header("Location: http://$site");
        exit;
    }
    else { // начало блока else
?>

<html> <head>
<title> Task 3.5 </title> </head>
<body>

    <?php
        print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";
        $sites_count = count($list_sites);
        $it=0;

        print "<select name=\"site\">\n";
        print "<option value =\"\">Search systems:";
        while($it<$sites_count) {
            print "<option value=\"$list_sites[$it]\">$list_sites[$it]";
            $it++;
        }
        print"</select>";
    ?>
    <input type="submit" value="Submit">
    </form>
<?php
     } // конец блока else
?>
</body>
</html>