#include <iostream>

int main()
{
	int n, m, check = 0, k = 0, out = 0;
	std::cin >> n;
	while (1)
	{
		check++;
		for (int i = check; i > 0; i /= 10)
		{
			if (i % 10 == 6)
			{
				k++;
				if (k == 3)
				{
					out++;
				}
			}
			else
			{
				k = 0;
			}
		}
		k = 0;
		if (out == n)
		{
			std::cout << check;
			return 0;
		}
	}
}
