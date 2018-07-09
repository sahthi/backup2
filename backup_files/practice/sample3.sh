echo "enter a number:"
read num
i=2
while ( $i -lt $num )
do
    if [ "expr $num % $i" -eq 0 ]
then
    echo"$num is not a prime numbert"
    fi 
    i= "expr $i + 1"
done
  

	
