<html> <head>
<title> Task 3.3 </title> </head> 
<body>

    <?php
        $user = $_POST["user"];
        $answers = $_POST["answers"];
        $otv = array("6","9","4","1","3","2","5","8","7");
        $count = 0;
        
        for($i=0; $i<9; $i++){
            if ($otv[$i] == $answers[$i]) {
                $count += 1;
            }
        }

        switch($count) {
            case 9:
                $result ="You know geography perfectly";
                break;
            case 8:
                $result ="You know geography excellent";
                break;
            case 7:
                $result ="You know geography very well";
                break;
            case 6:
                $result ="You know geography well";
                break;
            case 5:
                $result ="You know geography satisfactory";
                break;
            case 4:
                $result ="You know geography tolerably";
                break;
            case 3:
                $result ="You know geography bad";
                break;
            case 2:
                $result ="You know geography very bad";
                break;
            default:
                $result ="You don't know geography";
                break;
        }

        print "<p>User $user: $result";
    ?>
</body>
</html>