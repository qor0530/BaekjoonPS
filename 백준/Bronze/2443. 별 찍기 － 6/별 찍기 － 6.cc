#include <iostream>

using namespace std;

int main()
{
	int a, i, j, k, h;
	cin >> a;
	for (i = 0; i < a; i++)
	{
		for (j = 0;j < i;j++)
		{
			cout << " ";
		}
		for (k = i*2+1; k < (a*2);k++)
		{
			cout << "*";
		}
		cout << endl;
	}
}