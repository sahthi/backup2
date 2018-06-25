#include <stdio.h>
#include <string.h>
 
struct student 
{
     int empId;
     char empName[30];
     double salary;
};
 
int main() 
{
     int i,j;
     struct student record[10],temp;
 
     // 1st student's record
     record[0].empId=121;
     strcpy(record[0].empName, "Raju");
     record[0].salary = 8600;
 
     // 2nd student's record         
     record[1].empId=122;
     strcpy(record[1].empName, "Surendren");
     record[1].salary = 9000;
 
     // 3rd student's record
     record[2].empId=123;
     strcpy(record[2].empName, "suresh");
     record[2].salary = 8100;
 
	record[3].empId=124;
     strcpy(record[3].empName, "sathish");
     record[3].salary = 8300;
	 
	record[4].empId=125;
	strcpy(record[4].empName, "adithya");
     record[4].salary = 8500;
	 
	 record[5].empId=126;
     strcpy(record[5].empName, "trividi");
     record[5].salary = 8900;
	 
	 record[6].empId=127;
     strcpy(record[6].empName, "Thiyagu");
     record[6].salary = 9200;
	 
	 record[7].empId=129;
     strcpy(record[7].empName, "Nancy");
     record[7].salary = 9500;
	 
	 record[8].empId=130;
     strcpy(record[8].empName, "sampath");
     record[8].salary = 8900;
	 
	 record[9].empId=131;
     strcpy(record[9].empName, "pinky");
     record[9].salary = 8200;
     for(i=0; i<10; i++)
     {
         printf("     Records of STUDENT : %d \n", i+1);
         printf(" Id is: %d \n", record[i].empId);
         printf(" Name is: %s \n", record[i].empName);
         printf(" Percentage is: %lf\n\n",record[i].salary);
     }
     
     for(i=0;i<=10;i++)
     {
            for(j=0;j<=10;j++)
            {
                if(record[j].salary<record[j+1].salary)
                {
                  temp=record[j];
                  record[j]=record[j+1];
                  record[j+1]=temp;
                }
            }
     }
     printf("\nThe Sorted Salary is :\n");
     for(j=0;j<10;j++)
             printf("%d\t%s\t%lf\n",record[j].empId,record[j].empName,record[j].salary);
} 


