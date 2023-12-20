<html> <head>
    <title> Task 3.3</title> 
    <meta http-equiv="Content-Type" charset="windows-1251" />

</head> <body>
        <?php 
            $monuments = array(
                "Museum Prado",
                "Reichstag",
                "La Scala Opera House",
                "Bronze Horseman",
                "Wailing Wall",
                "Tretyakov's Gallery",
                "Arc de Triomphe",
                "Statue of Library",
                "Tower"
            );

            $options = "<select name=\"answers[]\" size=1>
                            <option value=\"\">located in the city
                            <option value=\"1\">St. Petersburg
                            <option value=\"2\">Moscow
                            <option value=\"3\">Jerusalem
                            <option value=\"4\">Milan
                            <option value=\"5\">Paris
                            <option value=\"6\">Madrid
                            <option value=\"7\">London
                            <option value=\"8\">New York
                            <option value=\"9\">Berlin
                        </select>";
        ?>
        
        <h2>Cities & monuments</h2>
        <form action="z4-3b.php" method="post">
            <p>Enter your name<p>
            <input type="text" name="user">
            <p>Determine which city this monument is located in<br>
            <p>
                <?php 
                    foreach($monuments as $it){
                        print "<p>$it $options</p>\n";
                    }
                ?>
            </p>
            <p><input type="submit" value="Check answers">
        </form>
    </body> </html>