read
read tp
for t in ${tp[@]};do
if [ -z $m ]||[[ ${t#-} -lt ${m#-} ]]||[[ ${t#-} -eq ${m#-}&&$m -lt $t ]];then
m=$t;fi;done
[[ -z $m ]]&&m=0
echo $m
