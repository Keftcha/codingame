read lX lY TX TY
idx_x=0;idx_y=0
while true;do
dir=""
((dep_x=$lX-$TX))
dep_x=${dep_x#-}
((dep_y=$lY-$TY))
dep_y=${dep_y#-}
if [ $idx_y -lt $dep_y ];then
if [ $TY -lt $lY ];then dir+="S";fi
if [ $TY -gt $lY ];then dir+="N";fi
((idx_y=$idx_y+1))
fi
if [ $idx_x -lt $dep_x ];then
if [ $TX -lt $lX ];then dir+="E";fi
if [ $TX -gt $lX ];then dir+="W";fi
(($idx_x++1))
fi
echo $dir
done
