read lightX lightY initialTX initialTY
idx_x=0
idx_y=0

while true; do
    read remainingTurns

    direction=()
    let "deplacement_x = $lightX - $initialTX"
    deplacement_x=${deplacement_x#-}
    let "deplacement_y = $lightY - $initialTY"
    deplacement_y=${deplacement_y#-}

    if [ $idx_y -lt $deplacement_y ]; then
        if [ $initialTY -lt $lightY ]; then
            direction=$direction"S"
        fi
        if [ $initialTY -gt $lightY ]; then
            direction=$direction"N"
        fi
        let "idx_y = $idx_y + 1"
    fi

    if [ $idx_x -lt $deplacement_x ]; then
        if [ $initialTX -lt $lightX ]; then
            direction=$direction"E"
        fi
        if [ $initialTX -gt $lightX ]; then
            direction=$direction"W"
        fi
        let "idx_x = $idx_x + 1"
    fi

    echo $direction
done
