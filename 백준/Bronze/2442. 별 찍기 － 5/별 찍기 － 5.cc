#include <iostream>

using namespace std;

int main()
{
	int a, i, j, k, h;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		for (j = a-1;j > i;j--)
		{
			cout << " ";
		}
		for (k = 0; k <= (i * 2);k++)
		{
			cout << "*";
		}
		cout << endl;
	}
}