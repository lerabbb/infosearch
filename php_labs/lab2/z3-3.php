
<html> <head>
<title> Task 2.5 </title>
</head> <body>

<?php
    function Ru($color) { print "<p><font color=\"$color\">Здравствуйте!</font>"; }
    function En($color) { print "<p><font color=\"$color\">Hello!</font>"; }
    function Fr($color) { print "<p><font color=\"$color\">Bonjour!</font>"; }
    function De($color) { print "<p><font color=\"$color\">Gutten Tag!</font>"; }

    $lang = $_GET["lang"];
    $color = $_GET["color"];
    switch($lang){
        case "ru": 
            Ru($color);
            break;
        case "en": 
            En($color);
            break;
        case "Fr": 
            Fr($color);
            break;
        case "De":
            De($color);
            break;
        default:
            print "unknown language";
            break;
    }
?>
</body> </html>