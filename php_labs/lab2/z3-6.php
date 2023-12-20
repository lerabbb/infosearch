<html> <head>
<title> Task 2.7 </title>
</head> 
<body>

    <?php
        function print_array($arr) {
            foreach ($arr as $key=>$value) {
                print "$key: $value; ";
            }
            print "<hr/>";
        }

        $cust = array (
            'cnum' => 2001,
            'cname' => "Hoffman",
            'city' => "London",
            'snum' => 1001,
            'rating' => 100
        );
        print_array($cust);
        asort($cust);
        print_array($cust);
        ksort($cust);
        print_array($cust);
        sort($cust);
        print_array($cust);
    ?>
</body> </html>

