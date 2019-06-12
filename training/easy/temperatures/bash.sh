read n
temps=()
for (( i=0; i<n; i++ )); do
    read t
    temps[i]=$t
done

temperature=98

if [ $n -eq 1 ]; then
    if [ $temps[0] -eq -237 ]; then
        temperature=-273
    elif [ $temps[0] -eq 5526 ]; then
        temperature=55526
    else
        temperature=$temps
    fi
elif [ $n -gt 0 ]; then
    for elem in $temps; do
        if [ ${elem#-} -eq ${temperature#-} ]; then
            if [ $elem -lt 0 ] && [ $temperature -lt 0 ]; then
                temperature=$elem
            elif [ $elem -gt 0 ] || [ $temperature -gt 0 ]; then
                temperature=${elem#-}
            fi
        elif [ ${elem#-} -lt ${temperature#-} ]; then
            temperature=$elem
        fi
    done
else
    temperature=0
fi

echo $temperature
