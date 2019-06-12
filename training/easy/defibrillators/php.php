<?php

function cal_dif($pa, $pb)
{
    $x = ($pb[0] - $pa[0]) * cos( ($pa[1] + $pb[1]) / 2);
    $y = $pb[1] - $pa[1];
    $dist = sqrt(($x**2) + ($y**2)) * 6371;
    return $dist;
}

function rem_vir($chaine)
{
    $chaine = str_split($chaine);
    foreach($chaine as $idx => $elem)
    {
        if ($elem == ",")
        {
            $chaine[$idx] = ".";
        }
    }
    return floatval(implode("", $chaine));
}


fscanf(STDIN, "%s",
    $LON
);
fscanf(STDIN, "%s",
    $LAT
);
fscanf(STDIN, "%d",
    $N
);

$liste_defib = array();
for ($i = 0; $i < $N; $i++)
{
    $DEFIB = stream_get_line(STDIN, 256 + 1, "\n");
    $liste_defib[] = $DEFIB;
}

foreach ($liste_defib as $idx => $defibrilateur)
{
    $liste_defib[$idx] = explode(";", $defibrilateur);
}

foreach ($liste_defib as $idx => $defibrilateur)
{
    $liste_defib[$idx][4] = rem_vir($defibrilateur[4]);
    $liste_defib[$idx][5] = rem_vir($defibrilateur[5]);
}

foreach ($liste_defib as $idx => $defibrilateur)
{
    $liste_defib[$idx][4] = deg2rad($defibrilateur[4]);
    $liste_defib[$idx][5] = deg2rad($defibrilateur[5]);
}

$lon = deg2rad(rem_vir($LON));
$lat = deg2rad(rem_vir($LAT));

$distance_mini = PHP_INT_MAX;

foreach ($liste_defib as $defibrilateur)
{
    if ($distance_mini > cal_dif(array ($lon, $lat), array ($defibrilateur[4],
$defibrilateur[5])))
    {
        $distance_mini = cal_dif(array ($lon, $lat), array ($defibrilateur[4],
$defibrilateur[5]));
        $defib_proche = $defibrilateur[1];
    }
}

echo($defib_proche);
?>
