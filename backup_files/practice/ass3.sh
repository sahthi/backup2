#!/bin/bash
#signal_test2.sh
trap exithandler
trap ' '
trap inthandler
Signal Handling
TERM
ABRT
INT
exithandler()
{
echo "Received SIGTERM"
exit 1
}
inthandler()
{
echo "Received SIGINT"
echo "Now making SIGINT to default action"
trap - INT # Restore the "INT" signal handler to the
default action
}
ps -f
cntr=1
echo "Welcome to Signal Handler
Program"
while true ;
do
echo -n $cntr
sleep 3
cntr=`expr $cntr + 1`
echo -n " "
done
