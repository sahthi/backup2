#include<stdio.h>
#define SIZE 10

int stack[SIZE];
int top=-1;

void push(int value)
{
	if(top<SIZE-1)
	{
		if(top<0)
		{
			stack[0]=value;
			top=0;
		}
		else
		{
			stack[top+1]=value;
			top++;
		}
	}
	else
	{	
		printf("stack overflow\n");
	}
}

int pop()
{
	if(top>=0)
	{
		int n = stack[top];
		top--;
		return n;
	}
}

int Top()
{
	return stack[top];
}

int isempty()
{
	return top<0;
}

void display()
{
	int i;
	for(i=0;i<top;i++)
	{
		printf("%d\n",stack[i]);
	}

}

int main()
{
	push(4);
	push(10);
	display();
	pop();
	display();
}








