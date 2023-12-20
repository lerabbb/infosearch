<html> <head>
<title> Task 2.6 </title>
</head> 
<body>

    <?php
        function print_array($arr) {
            foreach ($arr as $a)
                print $a."&nbsp&nbsp";
            print "<hr/>";
        }

        for ($n=1; $n<=10; $n++){
            $treug[$n-1] = $n*($n+1)/2;
        }
        print "treug: ";
        print_array($treug);

        for ($n=1; $n<=10; $n++){
            $kvd[$n-1] = $n*$n;
        }
        print "kvd: ";
        print_array($kvd);

        $res = array_merge($treug, $kvd);
        print "res - treug and kvd merge: ";
        print_array($res);

        sort($res);
        print "sorted res: ";
        print_array($res);

        array_shift($res);
        print "res without first element: ";
        print_array($res);

        $res1=array_unique($res);
        print "res1 - unique res: ";
        print_array($res1);
    ?>
</body> </html>

