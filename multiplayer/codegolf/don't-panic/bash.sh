read _ _ _ _ exp _ _ nbe
for((i=0;i<nbe;i++));do read elf elp;dic+=([${elf}]=$elp);done
while true;do
read cf clp dir;v=${dic[$cf]}
if [ -z $v ];then v=$exp;fi
if [[ ($clp -lt $v && $dir = "LEFT") || ($clp -gt $v && $dir = "RIGHT") ]];then echo "BLOCK"
else echo "WAIT";fi
done
