#include <iostream>

int main()
{
    long long int N, check, a[10] = { 0, };
    std::cin >> N;
    for (long long int i = N; i > 0; i /= 10)
    {
        check = i % 10;
        a[check]++;
    }
    for (int i = 9; i >= 0; i--)
    {
        while (a[i] > 0)
        {
            std::cout << i;
            a[i]--;
        }
    }
}