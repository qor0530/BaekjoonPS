#include <stdio.h>
#pragma warning(disable: 4996)
int main(void)
{
	int i, a[100], b[100], count;
	scanf("%d", &i);
	for (int num = 1; num <= i; num++)
	{
		scanf("%d %d", &a[num], &b[num]);
	}
	for (int num2 = 1; num2 <= i; num2++)
	{
		count = a[num2] + b[num2];
		printf("%d\n", count);
	}
	return 0;
}