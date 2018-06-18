declare -a liste_suivante
read R
read L

liste=( $R )

for (( i=1; i<$L; i++ )); do
    liste_suivante=()
    pr=0
    pb=0
    while [ $pb -lt ${#liste[@]} ]; do
        while [[ ($pr -lt ${#liste[@]}) && \
        (${liste[$pr]} -eq ${liste[$pb]}) ]]; do
            let "pr = $pr + 1"
        done
        let "nb = $pr - $pb"
        idx=${#liste_suivante[@]}
        liste_suivante[$idx]=$nb
        let "idx = $idx + 1"
        liste_suivante[$idx]=${liste[$pb]}
        pb=$pr
    done
    liste=( ${liste_suivante[@]} )
done

echo ${liste[@]}
