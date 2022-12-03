#include <stdio.h>
#pragma warning(disable:4996)
int main(void)
{
	int a, b, c;
	scanf("%d", &a);
	scanf("%d", &b);
	c = a * b;
	printf("%d\n", a * (b % 10));
	b /= 10;
	printf("%d\n", a * (b % 10));
	b /= 10;
	printf("%d\n", a * (b % 10));
	b /= 10;
	printf("%d\n", c);
	return 0;
}