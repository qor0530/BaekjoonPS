#include <iostream>

int main()
{
	int a, b, arr[100] = { 0, }, count, max = 0;
	std::cin >> a >> b;
	for (int i = 0; i < a; i++)
	{
		std::cin >> arr[i];
	}
	
	for (int i = 0; i < a; i++)
	{
		for (int j = i + 1; j < a; j++)
		{
			for (int k = j + 1; k < a; k++)
			{
				count = arr[i] + arr[j] + arr[k];
				if (count <= b && count > max)
					max = count;
			}
		}
	}
	std::cout << max << std::endl;
	return 0;
}
