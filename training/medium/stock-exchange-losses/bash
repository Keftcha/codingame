read n
read v
valeur=( $v )

perte=0

for nb in ${valeur[@]}; do
    if [ -z $vmax ] || [ $vmax -lt $nb ]; then
        vmax=$nb
        vmin=$nb
        continue;
    fi
    if [ $vmin -le $nb ]; then
        continue;
    fi
    vmin=$nb
    let "diff = $vmin - $vmax"
    if [ $diff -lt $perte ]; then
        perte=$diff
    fi
done

echo $perte
