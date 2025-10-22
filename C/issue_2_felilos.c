//Aproaching this calculator as single line user entry; user enters a string; prgramme concatinates string to pull apart digits and operator; programme caluclates result


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    double num1, num2, result; //using doubles instead of floats for extra accuracy
    char op = '\0'; //require this char type to get the symbol for calculations
    char input[100]; //limiting input as char array to 100 symbols
    char left[50], right[50];// left and right are going to be the numbers used for the calculation
    char choice;//the user's choice expressed in char Y/N to continue use of programme

    printf("   Simple Calculator (C version)\n");

    do {
        int i;
        int operatorPosition = -1; //initiate operator symbol as -1 to for the prorgamme to check later if oeprator valid
        int valid = 1; // initiate as true to use for validity check

        printf("\nEnter single-line calculation (e.g. 132/34): ");
        scanf("%s", input);

        // find the operator by checking for the first non-digit, non-decimal-point symbol
        for (i = 0; input[i] != '\0'; i++) {
            if (!isdigit((unsigned char)input[i]) && input[i] != '.') {
                op = input[i];
                operatorPosition = i;
                break;
            }
        }

        if (operatorPosition == -1) {
            printf("Error: No operator found!\n");
            continue;
        }

        // make the left and right substrings
        strncpy(left, input, operatorPosition);
        left[operatorPosition] = '\0';
        strcpy(right, input + operatorPosition + 1);

        if (strlen(left) == 0 || strlen(right) == 0) {
            printf("Error: Missing operand!\n");
            continue;
        }

        num1 = atof(left); //atof to change types to double
        num2 = atof(right);
	//and now let us find the case for the operator; execute the calculation
        switch (op) {
            case '+': result = num1 + num2; break;
            case '-': result = num1 - num2; break;
            case '*': result = num1 * num2; break;
            case '/':
                if (num2 != 0) //classic check
                    result = num1 / num2;
                else {
                    printf("Error: Division by zero!\n");
                    valid = 0;
                }
                break;
            default:
                printf("Error: Invalid operator '%c'!\n", op);
                valid = 0;
        }

        if (valid)
            printf("Result: %.6f\n", result); //double type allows for the 6 decimal places

        printf("\nDo another? (y/n): ");
        scanf(" %c", &choice);

    } while (choice == 'y' || choice == 'Y');

    printf("\nCalculator says G00dbye\n"); //Use 0 instead of Zeros for Fun
    return 0;
}
//#Hacktoberfest_2025
