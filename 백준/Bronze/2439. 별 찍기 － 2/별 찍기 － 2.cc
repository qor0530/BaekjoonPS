#include <iostream>

using namespace std;

int main()
{
	int a ,i, j, k;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		for (j = i+1;j < a; j++)
		{
			cout << " ";
		}
		for (k = 0;k <= i; k++)
		{
			cout << "*";
		}
		cout << endl;
	}
}