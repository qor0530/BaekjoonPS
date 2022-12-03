
#include <iostream>

int main()
{
	int a, b, c, num, numcount[10] = { 0 };
    std::cin >> a >> b >> c;
	num = a * b * c;
	while (num > 0)
	{
		switch (num % 10)
		{
		case 0:
			numcount[0]++;
			break;
		case 1:
			numcount[1]++;
			break;
		case 2:
			numcount[2]++;
			break;
		case 3:
			numcount[3]++;
			break;
		case 4:
			numcount[4]++;
			break;
		case 5:
			numcount[5]++;
			break;
		case 6:
			numcount[6]++;
			break;
		case 7:
			numcount[7]++;
			break;
		case 8:
			numcount[8]++;
			break;
		case 9:
			numcount[9]++;
			break;
		}
		num /= 10;
	}
	for (int i = 0; i < 10; i++)
	{
		std::cout << numcount[i] << std::endl;
	}
}
