<html> <head>
<title> Task 2.4 </title>
</head> 
<body>
    <?php
        print "<table border=1 cellpadding=5>\n";
        $color = 'blue';
        $base_color = "white";
        $plus_color = "red";
        for ($y=1;  $y <= 10;  $y++) {
            print "<tr>\n";
                for ($x=1;  $x <= 10;  $x++) {
                    print "\t<td>";
                    if($x==1 && $y==1) {
                        print "<p><font color=\"$color\">+</font>";
                    } elseif($x==1) {
                        print "<p><font color=\"$color\">$y</font>";
                    } elseif($y==1) {
                        print "<p><font color=\"$color\">$x</font>";
                    } else {
                        print ($x+$y);
                    }
                    print "</td>\n";
                }
                print "</tr>\n";
            }
        print "</table>";
    ?>
</body> </html>