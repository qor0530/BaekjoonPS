#include <stdio.h>
#pragma warning (disable : 4996)

int main(void)
{
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);

	if (a > 0 && b > 0)
	{
		printf("1");
	}
	if (a < 0 && b > 0)
	{
		printf("2");
	}
	if (a < 0 && b < 0)
	{
		printf("3");
	}
	if (a > 0 && b < 0)
	{
		printf("4");
	}
	return 0;
}