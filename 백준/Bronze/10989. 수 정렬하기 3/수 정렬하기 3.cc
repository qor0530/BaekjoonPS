#include <iostream>
#pragma warning(disable:4996)

#define MAX 10001

int N, num[MAX] = { 0, }, count, can;

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin >> N;
	for (int i = 0; i < N; i++)
	{
		std::cin >> count;
		num[count]++;
	}
	for (int i = 0; i < MAX; i++)
	{
		for (int j = 0; j < num[i]; j++)
		{
			std::cout << i << '\n';
		}
	}
	return 0;
}
