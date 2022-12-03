#include <iostream>
#include <iomanip>

int main()
{
	double N, sub[1000] = { 0.0f }, max, all = 0.0f, aver = 0.0f;
	std::cout.precision(8);
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> sub[i];
		if (i == 0)
		{
			max = sub[i];
		}
		else
		{
			if (sub[i] > max)
			{
				max = sub[i];
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		sub[i] = (sub[i] / max)* 100.0;
		all += sub[i];
	}
	aver = all / N;
	
	std::cout << aver;
}