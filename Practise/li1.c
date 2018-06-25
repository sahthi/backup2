#include<stdio.h>
#include<stdlib.h>

typedef struct node
{
	int a;
	struct node *next
}node;

node* push(int n,node *p)
{
	node *q;
	q=(node*)malloc(sizeof(node));
	q->a=n;
	q->next=p;
        return q;
}

node* pop(node *p)
{
	node *q;
	printf("popped element= %d",p->a);
        q=p;
	p=p->next;
	free(q);
	return p;
}

int main()
{
	node *p,*q;
	int n,ch;
	p=NULL;
	while(1)
	{
       	printf("\n Enter the operation number \n 1.PUSH  \n2.POP \n3.DISPLAY STACK");
        scanf("%d",&ch);
        if(ch == 1)
        {
		printf("enter the element:");
                scanf("%d",&n);
	        p=push(n,p);
 	}
	else if(ch == 2)
        {
		p=pop(p);
	}
	else if(ch == 3)
	{
		q=p;
		printf("\nstack: ");
                while(p!=NULL)
		{
			printf("\n%d",p->a);
			p=p->next;
		}
		p=q;
	}
	}
	return 0;
}


