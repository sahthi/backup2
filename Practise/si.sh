#!/bin/bash
echo "choose service provider [1.Airtel 2.Vodafone 3.AT&T]"
read opt
case $opt in
1) echo "you choose airtel"
;;
2) echo "you choose vodafone"
;;
3) echo "you choose AT&T"
;;
*) echo "Invalid Option"
;;
esac


