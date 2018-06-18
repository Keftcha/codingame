<?php
fscanf(STDIN, "%d",
    $R
);
fscanf(STDIN, "%d",
    $L
);

$liste = array();
$liste[] = $R;

for ($idx = 0; $idx < $L - 1; $idx += 1)
{
    error_log(var_export($idx, true));
    $liste_suivante = array();
    $pr = 0;
    $pb = 0;

    while ($pb<count($liste))
    {
        while (($pr < count($liste)) and ($liste[$pr] == $liste[$pb]))
        {
            $pr += 1;
        }
        $liste_suivante[] = $pr - $pb;
        $liste_suivante[] = $liste[$pb];
        $pb = $pr;
    }
    error_log(var_export($liste_suivante, true));
    $liste = $liste_suivante;

}
echo implode(" ", $liste);
?>
