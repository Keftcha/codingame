<?php
fscanf(STDIN, "%d",
    $n
);
$inputs = fgets(STDIN);
$inputs = explode(" ",$inputs);
$temp = array ();
for ($i = 0; $i < $n; $i++)
{
    $t = intval($inputs[$i]);
    $temp[] = $t;
}

usort($temp, function($a,$b) { return abs($a)<=>abs($b);});

if ($temp)
{
    if (abs($temp[0]) == abs($temp[1]))
    {
        echo max(array($temp[0], $temp[1]));
    }
    else
    {
        echo $temp[0];
    }
}
else echo 0;
?>
