// Write a program to make Simple calculator (to make addition, subtraction, multiplication, division and modulo)
#include <stdio.h>
void main()
{
    int k, j; 
    printf("Enter value of k: ");
    scanf("%d", &k); 
    printf("Enter value of j: ");
    scanf("%d", &j);                                    
    printf("\nAddition is: %d", k + j);                 
    printf("\nSubtraction is: %d", k - j);              
    printf("\nMultiplication is: %d", k * j);           
    printf("\nDivision is: %.1f", (float)k / (float)j); 
    printf("\nModulo is: %d", k % j);                   
}
