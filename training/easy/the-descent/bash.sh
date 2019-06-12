while true; do
    liste=()
    for (( i=0; i<8; i++ )); do
        read mountainH
        liste[i]=$mountainH
    done

    echo ${liste[*]} >&2

    haut=${liste[0]}
    for nb in ${liste[@]} ; do
        if [ $nb -gt $haut ] ; then
            haut=$nb
        fi
    done

    idx=0
    for nb in ${liste[@]} ; do
    if [ $nb -eq $haut ] ; then
        indice=$idx
        break
    fi
    let "idx = $idx + 1"
    done

    echo $indice

done
