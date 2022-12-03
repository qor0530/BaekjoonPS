#include <iostream>

int main()
{
	int a[1000], input, temp;

	std::cin >> input;
	for (int i = 0; i < input; i++)
	{
		std::cin >> a[i];
	}

	for (int i = 0; i < input; i++)
	{
		for (int j = i; j < input; j++)
		{
			if (a[i] > a[j])
			{
				temp = a[j];
				a[j] = a[i];
				a[i] = temp;
			}
		}
	}
	for (int i = 0; i < input; i++)
	{
		std::cout << a[i] << std::endl;
	}
	return 0;
}
