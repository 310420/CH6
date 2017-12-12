#include <stdio.h>
#include <stdlib.h>
#include "Information.h"

void main(void)
{
	Person P;
	
	printf("Please input your name:");
	scanf("%s", &P.name);
	printf("Please input your gender (0 for woman, 1 for man):");
	scanf("%d", &P.gender);
	printf("Please input your age:");
	scanf("%d", &P.age);

	printf("\nHi!%s. ",P.name);
	if (P.gender == 0)
		printf("You are a %d-year-old woman.\n", P.age);
	else
		printf("You are a %d-year-old man.\n", P.age);
	system("pause");
}