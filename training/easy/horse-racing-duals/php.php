<?php
fscanf(STDIN, "%d",
    $N
);
$liste_puissance = array ();
for ($i = 0; $i < $N; $i++)
{
    fscanf(STDIN, "%d",
        $Pi
    );
    $liste_puissance[] = $Pi;
}

sort($liste_puissance);
$diff = 98;
$idx = 0;

while ($idx + 1 < count($liste_puissance))
{
    if($diff > abs($liste_puissance[$idx] - $liste_puissance[$idx + 1]))
    {
        $diff = abs($liste_puissance[$idx] - $liste_puissance[$idx + 1]);
    }
    $idx += 1;
}

echo $diff;
?>
