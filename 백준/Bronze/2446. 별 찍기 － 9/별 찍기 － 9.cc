#include <iostream>

using namespace std;

int main()
{
	int a, i, j, k, h;
	cin >> a;
	for (i = a; i > 0; i--)
	{
		for (k = a; k > i; k--)
		{
			cout << " ";
		}
		for (j = 0; j < (i*2) - 1; j++)
		{
			cout << "*";
		}
		cout << endl;
	}
	for (i = 1; i < a; i++)
	{
		for (k = i; k < a-1; k++)
		{
			cout << " ";
		}
		for (j = (i * 2) + 1; j > 0; j--)
		{
			cout << "*";
		}
		cout << endl;
	}
}