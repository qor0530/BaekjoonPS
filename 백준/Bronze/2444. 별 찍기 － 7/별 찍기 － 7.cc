#include <iostream>

using namespace std;

int main()
{
	int a, i, j, k, h;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		for (j = i;j < a-1;j++)
		{
			cout << " ";
		}
		for (k = (i * 2); k >= 0;k--)
		{
			cout << "*";
		}
		cout << endl;
	}
	for (i = a-1; i > 0; i--)
	{
		for (j = a;j > i;j--)
		{
			cout << " ";
		}
		for (k = 0; k < (i*2)-1;k++)
		{
			cout << "*";
		}
		cout << endl;
	}

}