struct node
{
	int data;
	struct node *next;
}*top = NULL

void push(int);
void pop();
void display();

void main()
{
	int choice,value;
	printf("stack using linked list \n");
        while(1){
	     printf("1.push\n2.pop\n3.Display\n4.Exit\n");
             printf("enter ur choice:");
             scanf("%d",&choice);
	     switch(choice)
             {
                  case1:printf("enter the value to insert");
                        scanf("%d",&value);
                        push(value);
			break;
                  case2:pop();
                        break;
                  case3:display();
                        break;
                  case4:exit(0);
                  default:printf("wrong selection!!!please try again!!!\n");
              }
           }
        }
void push(int value)
{
	struct node *newnode;
        newnode=(struct node*)malloc(size of (struct node));
        newnode->data=value;
        if(top==NULL)
            newnode->next = NULL;
        else
	    newnode->next = top;
        top=newnode;
        printf("\n Insertion is success!!!\n");
}

void pop()
{
	if(top==NULL)
            printf("stack is empty\n");
        else{
            struct node *temp=top;
            top=temp->next;
            free(temp);
        }
     }
void display()
{
	if(top==NULL)
            printf("stack is empty\n");
        else{
            struct Node *temp = top;
        while(temp->next != NULL){
	    printf("%d--->",temp->data);
	    temp = temp -> next;
      }
        printf("%d--->NULL",temp->data);
   }
}



























  


        

	


