

#include<stdio.h>
struct employee
{
     int eno;
     char ename[20];
     int salary;
}emp[10];
int main()
{
     int i,high,n;
     printf("/*How many employee info\nyou want to accept : ");
     printf("Enter Limit: ");
     scanf("%d",&n);
     printf("-----------------------------\n");
     printf("Enter details for %d employees:",n);
     printf("\n-----------------------------\n");
     for(i=0;i<n;i++)
     {
          printf("Employee Number: ");
          scanf("%d",&emp[i].eno);
          printf("Name           : ");
          scanf("%s",emp[i].ename);
          printf("Salary         : ");
          scanf("\n %d",&emp[i].salary);
          printf("-----------------------------\n");
     }
    
void display(struct student list[80], int s)
{
    int i;
    
    printf("\n\nRollno\tName\tMarks\n");
    for (i = 0; i < s; i++)
    {
        printf("%d\t%s\t%d\n", emp[i].eno, emp[i].ename, emp[i].salary);
    } 
}

void bsortDesc(struct student list[80], int s)
{
    int i, j;
    struct student temp;
    
    for (i = 0; i < s - 1; i++)
    {
        for (j = 0; j < (s - 1-i); j++)
        {
            if (list[j].marks < list[j + 1].marks)
            {
                temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            } 
        }
    }
}
