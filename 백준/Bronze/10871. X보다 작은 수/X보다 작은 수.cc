#include <stdio.h>
#pragma warning(disable: 4996)
int main(void)
{
	int a, b, arr[10000];
	scanf("%d %d", &a, &b);
	for (int i = 1; i <= a; i++)
	{
		scanf("%d", &arr[i]);
	}
	for (int i = 1; i <= a; i++)
	{
		if (arr[i] < b)
		{
			printf("%d ", arr[i]);
		}
	}
	return 0;
}