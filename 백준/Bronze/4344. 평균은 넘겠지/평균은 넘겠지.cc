#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n;
	double score[1000],sum = 0, arge, upto, student, count = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> student;
		for (int j = 0; j < student; j++)
		{
			cin >> score[j];
			sum += score[j];
		}  
		arge = sum / student;

		for (int k = 0; k < student; k++)
		{
			if (score[k] > arge)
			{
				count++;
			}
		}
		upto = (count / student)*100;
		cout.setf(ios::fixed);
		cout.precision(3);
		cout << upto << "%\n";
		count = 0;
		sum = 0;
	}

}