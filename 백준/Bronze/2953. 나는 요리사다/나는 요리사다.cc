#include <iostream>

int main()
{
	int a[5][4], max = 0, max_line, score;
	for (int i = 0; i < 5; i++)
	{
		score = 0;
		for (int j = 0; j < 4; j++)
		{
			std::cin >> a[i][j];
			score += a[i][j];
		}
		if (score > max)
		{
			max = score;
			max_line = i + 1;
		}
	}

	std::cout << max_line << " " << max;
	return 0;
}
