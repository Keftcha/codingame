<?php
$dico = array ();

fscanf(STDIN, "%d %d %d %d %d %d %d %d",
    $nbFloors, // number of floors
    $width, // width of the area
    $nbRounds, // maximum number of rounds
    $exitFloor, // floor on which the exit is found
    $exitPos, // position of the exit on its floor
    $nbTotalClones, // number of generated clones
    $nbAdditionalElevators, // ignore (always zero)
    $nbElevators // number of elevators
);
for ($i = 0; $i < $nbElevators; $i++)
{
    fscanf(STDIN, "%d %d",
        $elevatorFloor, // floor on which this elevator is found
        $elevatorPos // position of the elevator on its floor
    );
    $dico[$elevatorFloor] = $elevatorPos;
}

while (TRUE)
{
    fscanf(STDIN, "%d %d %s",
        $cloneFloor, // floor of the leading clone
        $clonePos, // position of the leading clone on its floor
        $direction // direction of the leading clone: LEFT or RIGHT
    );

    $valeur = $dico[$cloneFloor];
    if (!$valeur) $valeur = $exitPos;

    if ($clonePos > $valeur && $direction == "RIGHT") $instruction = "BLOCK";
    elseif ($clonePos < $valeur && $direction == "LEFT") $instruction =
"BLOCK";
    else $instruction = "WAIT";

    echo($instruction . "\n"); // action: WAIT or BLOCK
}
?>
