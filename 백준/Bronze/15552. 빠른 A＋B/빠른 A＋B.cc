#include <iostream>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int a, x, y, ary1;
	cin >> a;
	for (int i = 0;i<a; i++)
	{
		cin >> x >> y;
		ary1 = x + y;
		cout << ary1<<"\n";
	}
}