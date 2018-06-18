declare -A dico

read nbFloors width nbRounds exitFloor exitPos nbTotalClones
nbAdditionalElevators nbElevators
for (( i=0; i<nbElevators; i++ )); do
    read elevatorFloor elevatorPos
    dico+=([${elevatorFloor}]=$elevatorPos)
done

while true; do
    read cloneFloor clonePos direction

    valeur=${dico[$cloneFloor]}
    if [ -z $valeur ]; then
        valeur=$exitPos
    fi

    if [ $clonePos -lt $valeur ] && [ $direction = "LEFT" ]; then
        instruction="BLOCK"
    elif [ $clonePos -gt $valeur ] && [ $direction = "RIGHT" ]; then
        instruction="BLOCK"
    else
        instruction="WAIT"
    fi

    echo $instruction
done
