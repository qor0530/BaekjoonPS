#include <iostream>

using namespace std;

int main()
{
	int a, i, j;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		for (j = a - 1;j >= i; j--)
		{
			cout << "*";
		}
		cout << endl;
	}
}