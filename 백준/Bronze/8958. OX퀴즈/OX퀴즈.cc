#include <iostream>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n, hit = 0,score = 0, k = 0;
	string a;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		while (1)
		{
			if (a[k] == 'O')
			{
				score++;
				score += hit;
				hit++;
			}
			else if (a[k] == 'X')
			{
				hit = 0;
			}
			else
			{
				k = 0;
				cout << score << "\n";
				hit = 0;
				score = 0;
				break;
			}
			k++;
		}
	}
}