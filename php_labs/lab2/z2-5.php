<html> <head>
<title> Task 2.2 </title> </head> <body> 

<?php 
    $lang = $_GET['lang'];

    switch($lang){
        case "ru": 
            print "russian"; 
            break;
        case "en": 
            print "english";
            break;
        case "Fr": 
            print "french";
            break;
        case "De": 
            print "dutch";
            break;
        default: 
            print "unknown language";
            break;
    }
?>
</body> </html>