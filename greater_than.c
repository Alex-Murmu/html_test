#include<stdio.h>
int main()
{
    /*find max of A and B*/
    int A,B;
    printf("Enter the number A\n");
    scanf("%d",&A);
    printf("Enter the number B\n");
    scanf("%d",&B);
   if (A<B)
   {
    printf("B is max %d",B);
   }
   else
   {
    printf("A is max %d",A);
   }
   
}