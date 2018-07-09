echo "Enter a file name "
read filename
if [ ! -f $filename ]
then
echo "Sorry, file does'nt exist"
exit
fi
echo "Enter cmd [cat/wc/sort/rm/ls] to run on the file : "
read cmd
case $cmd in
"cat"|"wc"|"sort") $cmd $filename
;;
"rm") $cmd -i $filename
;;
"ls") $cmd -l $filename
;;
*) echo "Error: cmd not in selection list"
;;
esac
