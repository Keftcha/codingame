read
read e
for t in ${e[@]};do
if [ -z $m ]||[[ ${t#-} -lt ${m#-} ]]||[[ ${t#-} == ${m#-}&&$m < $t ]];then
m=$t;fi;done
[[ -z $m ]]&&m=0
echo $m
