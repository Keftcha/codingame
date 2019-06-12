<?php
fscanf(STDIN, "%d",
    $n
);
$inputs = fgets(STDIN);
$inputs = explode(" ",$inputs);
$valeurs = array();
for ($i = 0; $i < $n; $i++)
{
    $v = intval($inputs[$i]);
    $valeurs[] = $v;
}

$pertes = 0;
foreach ($valeurs as $nb)
{
    if (!($vmax) or $vmax < $nb)
    {
        $vmax = $nb;
        $vmin = $nb;
        continue;
    }
    if ($vmin <= $nb)
    {
        continue;
    }
    $vmin = $nb;
    $diff = $vmin - $vmax;
    if ($diff<$pertes)
    {
        $pertes = $diff;
    }
}
echo($pertes);
?>
