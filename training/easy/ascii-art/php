<?php
fscanf(STDIN, "%d",
    $L
);
fscanf(STDIN, "%d",
    $H
);
$T = stream_get_line(STDIN, 256 + 1, "\n");
$T = strtoupper($T);
for ($i = 0; $i < $H; $i++)
{
    $ROW = stream_get_line(STDIN, 1024 + 1, "\n");

    for ($idx = 0; $idx < strlen($T); $idx+=1)
    {
        $lettre = $T[$idx];
        $lettre_nb = ord($lettre) - 65;
        if ($lettre_nb > 25 or $lettre_nb < 0)
        {
            $lettre_nb = 26;
        }

        for ($char = 0; $char < $L; $char += 1)
        {
            print($ROW[($lettre_nb * $L) + $char]);
        }
    }
    print("\n");
}
?>
