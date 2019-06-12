read l
read h
read t
IFS=""
t=${t^^}

for (( i=0; i<h; i++ )); do
    read -r ROW
    for (( idx=0; idx<${#t}; idx++ )); do
        lettre=${t:$idx:1}
        let "lettre_nb = `printf "%d\n" \'$lettre` - 65" # le -65 est merdique
        [[ $lettre != [A-Z] ]] && lettre_nb=26 # equivalent d'un if [ ]; then;
do ... fi
        let "debut_lettre = $lettre_nb * $l"
        echo -n "${ROW:$debut_lettre:$l}"
    done
    echo
done
