#include <iostream>

using namespace std;

int main()
{
	int a, i, j, k, h;
	cin >> a;
	for (i = a; i > 0; i--)
	{
		for (j = a;j >= i;j--)
		{
			cout << "*";
		}
		for (k = (i*2)-2;k>0;k--)
		{
			cout << " ";
		}
		for (j = a;j >= i;j--)
		{
			cout << "*";
		}
		cout << endl;
	}
	for (i = 1; i < a; i++)
	{
		for (j = i;j <= a-1;j++)
		{
			cout << "*";
		}
		for (k = (i * 2) ; k > 0;k--)
		{
			cout << " ";
		}
		for (j = i;j <= a - 1;j++)
		{
			cout << "*";
		}
		cout << endl;
	}


}