<?php
fscanf(STDIN, "%d",
    $N
);
$dictionaire = array();

for ($i = 0; $i < $N; $i++)
{
    $W = stream_get_line(STDIN, 30 + 1, "\n");
    $dictionaire[] = $W;
}
$LETTERS = stream_get_line(STDIN, 8 + 1, "\n");

$mot_possible = array ();
foreach($dictionaire as $mot)
{
    $liste = str_split($LETTERS);
    $passe = true;
    foreach (str_split($mot) as $lettre)
    {
        if (in_array($lettre, $liste))
        {
            unset($liste[array_search($lettre, $liste)]);
            continue;
        }
        $passe = false;
        break;
    }
    if ($passe == true)
    {
        $mot_possible[] = $mot;
    }
}

$points = 0;
$mots = array();
for ($idx = 0; $idx < count($mot_possible); $idx += 1)
{
    $pts = 0;
    $mot = $mot_possible[$idx];
    foreach(str_split($mot) as $lettre)
    {
        if (in_array($lettre, array("e", "a", "i", "o", "n", "r", "t", "l",
"s", "u")))
        {
            $pts += 1;
        }
        else if (in_array($lettre, array("d", "g")))
        {
            $pts += 2;
        }
        else if (in_array($lettre, array("b", "c", "m", "p")))
        {
            $pts += 3;
        }
        else if (in_array($lettre, array("f", "h", "v", "w", "y")))
        {
            $pts += 4;
        }
        else if (in_array($lettre, array("k")))
        {
            $pts += 5;
        }
        else if (in_array($lettre, array("j", "x")))
        {
            $pts += 8;
        }
        else if (in_array($lettre, array("q", "z")))
        {
            $pts += 10;
        }
    }
    if ($pts > $points)
    {
        $points = $pts;
        $index = $idx;
    }
}

echo $mot_possible[$index];
?>
