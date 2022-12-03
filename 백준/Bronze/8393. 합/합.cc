#include <stdio.h>
#pragma warning(disable:4996)

int main(void)
{
	int i, count = 0;
	scanf("%d", &i);
	for (int k = 1; k <= i; k++)
	{
		count = count + k;
	}
	printf("%d", count);
	return 0;
}