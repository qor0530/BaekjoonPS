#include <iostream>

using namespace std;

int main()
{
	int a, i, j, k;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		for (k = 0;k < i; k++)
		{
			cout << " ";
		}
		for(j = a - 1;j >= i; j--)
		{
			cout << "*";
		}
		cout << endl;
	}
}