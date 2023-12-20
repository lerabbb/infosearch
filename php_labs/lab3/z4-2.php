<html>
<head>
    <title> Task 3.2 </title>
</head>
<body>
    <?php
        $align= (isset($_POST["align"])) ? $_POST["align"] : 'left';
        $valign= (isset($_POST["valign"])) ? $_POST["valign"] : 'top';
        print "<table border=1 width=100; height=100'>\n";
        print "<tr><td align='$align' valign='$valign'>Text</td></tr></table>\n";
        print "<a href='z4-1a.htm'>back</a>";
    ?>

    <form action="z4-2.php" method="POST">
        <p><b>Select horizontal position:</b></p>
        <p><input type="radio" name="align" value="left">left</p>
        <p><input type="radio" name="align" value="center">centered</p>
        <p><input type="radio" name="align" value="right">right</p>

        <p><b>Select vertical position:</b></p>
        <p><input type="radio" name="valign" value="top">top</p>
        <p><input type="radio" name="valign" value="middle">centered</p>
        <p><input type="radio" name="valign" value="bottom">bottom</p>
        <p><input type="submit" value="Submit"></p>
    </form>
</body>
</html>