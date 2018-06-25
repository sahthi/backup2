#include<stdio.h>
struct employee
{
          int eno;
          char ename[20];
          long int salary;
};
void  main()

{   
     struct employee e[20],temp;
     int i,j,n;
     printf("/*How many employee info\nyou want to accept : ");
     printf("Enter Limit: ");
     scanf("%d",&n);
     printf("-----------------------------\n");
     printf("Enter details for %d employees:",n);
     printf("\n-----------------------------\n");
     for(i=0;i<n;i++)
     {
          printf("Employee Number: ");
          scanf("%d",&e[i].eno);
          printf("Name           : ");
          scanf("%s",e[i].ename);
          printf("Salary         : ");
          scanf("\n %ld",&e[i].salary);
          printf("-----------------------------\n");
     }
     for(i=0;i<=n-1;i++)
     {
            for(j=0;j<=n-1;j++)
            {
                if(e[j].salary<e[j+1].salary)
                {
                  temp=e[j];
                  e[j]=e[j+1];
                  e[j+1]=temp;
                }
            }
     }
     printf("\nThe Sorted Salary is :\n");
     for(j=0;j<n;j++)
	     printf("%d\t%s\t%ld\n",e[j].eno,e[j].ename,e[j].salary);
} 



