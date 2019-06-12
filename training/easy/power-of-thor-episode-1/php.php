<?php
fscanf(STDIN, "%d %d %d %d",
    $light_x,
    $light_y,
    $initial_tx,
    $initial_ty
);

$idx_x = 0;
$idx_y = 0;

while (TRUE)
{
    fscanf(STDIN, "%d",
        $remainingTurns
    );

    $direction = array ();
    $deplacement_x = abs($light_x - $initial_tx);
    $deplacement_y = abs($light_y - $initial_ty);

    if ($idx_y < $deplacement_y)
    {
        if ($initial_ty < $light_y)
        {
            $direction[] = "S";
        }
        if ($initial_ty > $light_y)
        {
            $direction[] = "N";
        }
        $idx_y += 1;
    }

    if ($idx_x < $deplacement_x)
    {
        if ($initial_tx < $light_x)
        {
            $direction[] = "E";
        }
        if ($initial_tx > $light_x)
        {
            $direction[] = "W";
        }
        $idx_x += 1;
    }

    print(implode("", $direction) . "\n");
}
?>
