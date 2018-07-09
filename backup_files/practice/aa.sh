#!/bin/bash
#signal_test1.sh
trap exithandler
trap ' '
trap inthandler
trap usrhandler
Signal Handling
TERM
QUIT
INT
SIGUSR1 SIGUSR2
exithandler()
{
echo "Received SIGTERM"
exit 1
}
inthandler()
{
echo "Received SIGINT"
}
usrhandler()
{
echo "Received SIGUSR1 or SIGUSR2"
}
while true ;
do
echo "Welcome"
sleep 3
ps -f
done
