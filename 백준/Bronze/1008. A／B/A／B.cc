#include <stdio.h>
#pragma warning(disable:4996)

int main(void)
{
	double a, b, c;
	scanf("%lf %lf", &a, &b);
	c = a / b;
	printf("%.9f", c);
	return 0;
}