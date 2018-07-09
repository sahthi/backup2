echo "Choose service provider [1.Airtel 2.Vodafone 3.AT&T] :"
read opt
case $opt in
1) echo "You chose Airtel"
;;
2) echo "You chose Vodafone"
;;
3) echo "You chose AT&T"
;;
*) echo "Invalid option"
;;
esac
