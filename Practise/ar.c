#include<stdio.h>
#define MAX 5

int top=-1;
int stack_arr[MAX];

void push()
{
	int p;
	if (top == (MAX-1))
		printf("stack Overflow\n");
	else
        {
		printf("enter the item to be pushed onto stack:");
		scanf("%d",&p);
		top=top+1;
		stack_arr[top]=p;
	}
}
void pop()
{
	if(top == -1)
		printf("stack underflow\n");
	else
	{

		printf("popped element is:%d",stack_arr[top]);
		top=top-1;

        }


void display()
{	
	int i;
	if(top == -1)
		printf("stack is empty \n");
	else
	{
		printf("stack elements are:");
		for(i=top;i>=0;i--)
			printf("%d\n",stack_arr[i]);
	}
}

main()
{
	int choice;

	do{
		printf("1.Push\n");
		printf("2.Pop\n");
		printf("3.Display\n");
		printf("4.Quit\n");
		printf("Enter your choice : ");
		scanf("%d",&choice);
		switch(choice)
		{
		 case 1 :
			push();
			break;
		 case 2:
			pop();
			break;
		 case 3:
			display();
			break;
		 case 4:
                        break;
		 default:
			printf("Wrong choice\n");
		}}while(choice!=4);
}


