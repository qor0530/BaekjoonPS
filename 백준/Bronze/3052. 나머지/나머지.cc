#include <iostream>

int main()
{
	int remain[42] = { 0 }, Check = 0, input[10];
	


	for (int i = 0; i < 10; i++)
	{
		std::cin >> input[i];
		remain[input[i] % 42]++;
	}
	
	for (int i = 0; i < 42; i++)
	{
		if (remain[i] > 0)
			Check++;
	}
	std::cout << Check;
}