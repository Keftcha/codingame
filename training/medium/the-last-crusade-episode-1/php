<?php
fscanf(STDIN, "%d %d",
    $W, // number of columns.
    $H // number of rows.
);
$terrain = array();
for ($i = 0; $i < $H; $i++)
{
    $LINE = stream_get_line(STDIN, 200 + 1, "\n"); // represents a line in the
grid and contains W integers. Each integer represents one room of a given type.
    $terrain[] = explode(" ", $LINE);
}
fscanf(STDIN, "%d",
    $EX // the coordinate along the X axis of the exit (not useful for this
first mission, but must be read).
);

while (TRUE)
{
    fscanf(STDIN, "%d %d %s",
        $XI,
        $YI,
        $POS
    );

    $x = $XI;
    $y = $YI;

    if ($terrain[$y][$x] == "1" or $terrain[$y][$x] == "3" or $terrain[$y][$x]
== "7" or $terrain[$y][$x] == "8" or $terrain[$y][$x] == "9" or
$terrain[$y][$x] == "12" or $terrain[$y][$x] == "13")
    {
        $y += 1;
    }
    else if ($POS == "TOP" and ($terrain[$y][$x] == "4" or $terrain[$y][$x] ==
"10"))
    {
        $x -= 1;
    }
    else if ($POS == "TOP" and ($terrain[$y][$x] == "5" or $terrain[$y][$x] ==
"11"))
    {
        $x += 1;
    }
    else if ($POS == "LEFT" and ($terrain[$y][$x] == "2" or $terrain[$y][$x] ==
"6"))
    {
        $x += 1;
    }
    else if ($POS == "LEFT" and ($terrain[$y][$x] == "5"))
    {
        $y += 1;
    }
    else if ($POS == "RIGHT" and ($terrain[$y][$x] == "2" or $terrain[$y][$x]
== "6"))
    {
        $x -= 1;
    }
    else if ($POS == "RIGHT" and ($terrain [$y][$x] == "4"))
    {
        $y += 1;
    }
    echo($x . " " . $y . "\n");
}
?>
