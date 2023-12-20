
<html>
<head>
    <title> Task 3.1 </title>
</head>
<body>
    <?php
        $align= $_POST["align"];
        $valign= $_POST["valign"];
        print "<table border=1 width=100; height=100'>\n";
        print "<tr><td align='$align' valign='$valign'>Text</td></tr></table>\n";
        print "<a href='z4-1a.htm'>back</a>";
    ?>
</body>
</html>