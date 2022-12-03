#include <stdio.h>

int main(void)
{
	int x, y, w, h;
	int height = 0, width = 0;
	int minimun = 0;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	if (w - x > x)
		width = x;
	else
		width = w - x;

	if (h - y > y)
		height = y;
	else
		height = h - y;

	if (width > height)
		minimun = height;
	else
		minimun = width;

	printf("%d", minimun);
}