#include<stdio.h>
void main()
{
unsigned int number;
int i=0,hexadecimal,rev=0,bit,NUM_BITS_INT;
printf("enter the hexadecimal value:");
scanf("0x%number",&hexadecimal);
while(i++<NUM_BITS_INT)
{
   bit=hexadecimal&1;
   hexadecimal=hexadecimal>>1;
   rev =rev^bit;
}
if(i<NUM_BITS_INT)
{
    rev=rev<<1;
}
printf("reverse of hexadecimal value is 0x%number:",rev);
}



