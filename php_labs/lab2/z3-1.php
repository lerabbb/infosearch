<html> <head>
<title> Task 2.3 </title>
</head> 
<body>
    <?php
        print "<table border=1 cellpadding=5>\n";
        $base_color = "white";
        $diagonal_color = "grey";
        for ($y=1;  $y <= 10;  $y++) {
            print "<tr>\n";
                for ($x=1;  $x <= 10;  $x++) {
                    $color= ($x==$y) ? $diagonal_color : $base_color;
                    
                    print "\t<td style=\"background:$color\">";
                    print ($x*$y);
                    print "</td>\n";
                }
                print "</tr>\n";
            }
        print "</table>";
    ?>
</body> </html>