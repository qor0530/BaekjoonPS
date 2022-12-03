
#include <iostream>

int main()
{
	int output, decom, length = 1, check = 0, num;
	std::cin >> decom;

	for (int i = decom; i / 10 > 0; i /= 10)
	{
		length++;
	}

	output = decom - length * 9;
	while (1)
	{
		if (output == decom)
		{
			std::cout << "0";
			return 0;
		}
		num = 0;
		for (int i = output; i % 10 > 0; i /= 10)
		{
			num = num + i % 10;
		}
		check = output + num;
		if (check == decom)
		{
			break;
		}
		output++;
	}
	std::cout << output;

	return 0;
}

