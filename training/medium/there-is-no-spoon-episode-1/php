<?php
fscanf(STDIN, "%d",
    $width // the number of cells on the X axis
);
fscanf(STDIN, "%d",
    $height // the number of cells on the Y axis
);

$grille = array();

for ($i = 0; $i < $height; $i++)
{
    $line = stream_get_line(STDIN, 31 + 1, "\n"); // width characters, each
either 0 or .
    $grille[] = $line;
}

$colone = 0;
$ligne = 0;
$nb_colone = $width;
$nb_ligne = $height;

$liste_neuds = array();
for ($nb = 0; $nb < $nb_ligne; $nb += 1)
{
    for ($nombre = 0; $nombre < $nb_colone; $nombre += 1)
    {
        if ($grille[$nb][$nombre] == "0")
        {
            $new = array($nombre, $nb);
            $liste_neuds[] = array($nombre, $nb);
        }
    }
}

for ($idx = 0; $idx < count($liste_neuds); $idx += 1)
{
    $neud = $liste_neuds[$idx];
    $affiche = "";
    $affiche = $affiche . " " . $neud[0] . " " . $neud[1];

    $index = $idx + 1;
    $passage = true;
    while ($index < count($liste_neuds))
    {
        if ($neud[1] == $liste_neuds[$index][1])
        {
            $affiche = $affiche . " " . $liste_neuds[$index][0] . " " .
$liste_neuds[$index][1];
            $passage = false;
            break;
        }
        $index += 1;
    }
    if ($passage == true)
    {
        $affiche = $affiche . " -1 -1";
    }

    $index2 = $idx + 1;
    $passage2 = true;
    while ($index2 < count($liste_neuds))
    {
        if ($neud[0] == $liste_neuds[$index2][0])
        {
            $affiche = $affiche . " " . $liste_neuds[$index2][0] . " " .
$liste_neuds[$index2][1];
            $passage2 = false;
            break;
        }
        $index2 += 1;
    }
    if ($passage2 == true)
    {
        $affiche = $affiche . " -1 -1";
    }

    echo ($affiche);
    echo "\n";
}
?>
