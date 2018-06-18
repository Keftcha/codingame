read N
read Q

declare -A dico_types
liste_fichiers=()

for (( i=0; i<N; i++ )); do
    read EXT MT
    dico_types+=([${EXT,,}]=$MT)
done

echo ${dico_types[@]} >&2
echo ${!dico_types[@]} >&2


for (( i=0; i<Q; i++ )); do
    read fichier

    file=${fichier%.*}

    extention=${fichier:${#file} + 1}
    extention=${extention,,}
    echo $file $extention >&2
    if  [ -z $extention ] || [ -z ${dico_types[$extention]} ]; then
        echo "UNKNOWN"
    else
        echo ${dico_types[$extention]}
    fi

done
