read W H

terrain=()

for (( i=0; i<H; i++ )); do
    read LINE
    line=$LINE
    terrain[$i]=$line

done

echo ${terrain[@]} >&2

read EX

while true; do
    read x y pos

    echo $x $y $pos >&2

    line=( ${terrain[$y]} )
    echo ligne "${line[x]}" >&2

    if [ "${line[x]}" = "1" ] || [ "${line[x]}" = "3" ] || [ "${line[x]}" = "7"
] || [ "${line[x]}" = "8" ] || [ "${line[x]}" = "9" ] || [ "${line[x]}" = "12"
] || [ "${line[x]}" = "13" ]; then
        let "y = $y + 1"
    elif [[ ($pos = "TOP") && ("${line[x]}" = "4" || "${line[x]}" = "10") ]];
then
        let "x = $x - 1"
    elif [[ ($pos = "TOP") && ("${line[x]}" = "5" || "${line[x]}" = "11") ]];
then
        let "x = $x + 1"
    elif [[ ($pos = "LEFT") && ("${line[x]}" = "2" || "${line[x]}" = "6")
]];then
        let "x = $x + 1"
    elif [ $pos = "LEFT" ] && [ "${line[x]}" = "5" ]; then
        let "y = $y + 1"
    elif [[ ( $pos = "RIGHT") && ("${line[x]}" = "2" || "${line[x]}" = "6") ]];
then
        let "x = $x - 1"
    elif [ $pos = "RIGHT" ] && [ "${line[x]}" = "4" ]; then
        let "y = $y + 1"
    fi

    echo $x $y >&2
    echo $x $y
done
