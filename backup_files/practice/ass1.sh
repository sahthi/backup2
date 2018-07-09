echo "enter values:"
read v1
read v2
echo "choose arithmetic operations: 1.sum 2.sub 3.mul 4.div 5.div"
read opt
case $opt in
1)echo sum=`expr $v1 + $v2`
  echo $sum
;;
2)echo sub= `expr $v1 - $v2`
  echo $sub
;;
3)echo mul=`expr $v1 \* $v2`
  echo $mul
;;
4)echo div=`expr $v1 / $v2`
  echo $div
;;
5)echo rem=`expr $v1 % $v2`
  echo $rem
;;
esac
 
 
	
