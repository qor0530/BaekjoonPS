#include <stdio.h>
#pragma warning(disable:4996)

int main(void)
{
	int hour, minute, setmin = 60;
	scanf("%d %d", &hour, &minute);
	if (hour != 0)
	{
		if (minute < 45)
		{
			minute = minute - 45;
			hour--;
			setmin = setmin + minute;
			minute = setmin;
		}
		else
		{
			minute = minute - 45;
		}
	}
	else
	{
		if (minute < 45)
		{
			hour = 24;
			minute = minute - 45;
			hour--;
			setmin = setmin + minute;
			minute = setmin;
		}
		else
		{
			minute = minute - 45;
		}
	}
	printf("%d %d", hour, minute);
	return 0;
}