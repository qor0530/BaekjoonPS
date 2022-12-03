#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool change(pair <int, string> a, pair <int, string> b)
{
	return a.first < b.first;
}
int main()
{
	int N, x;
	string y;
	cin >> N;
	vector<pair <int, string>> A(N);
	for (int i = 0; i < N; i++) {
		cin >> A[i].first >> A[i].second;
	}
	stable_sort(A.begin(), A.end(), change);

	for (int i = 0; i < N; i++)
	{
		cout << A[i].first << " " << A[i].second << "\n";
	}
}