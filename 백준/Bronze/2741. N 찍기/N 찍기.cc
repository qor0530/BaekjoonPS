#include <stdio.h>
#pragma warning(disable: 4996)
int main(void)
{
	int a;
	scanf("%d", &a);
	for (int i = 1; i <= a; i++)
	{
		printf("%d\n", i);
	}
	return 0;
}