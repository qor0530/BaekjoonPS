#include <iostream>

int main()
{
    int weight[50], height[50], man, ranking[50] = { 0 };
    std::cin >> man;
    for (int i = 0; i < man; i++)
    {
        std::cin >> weight[i] >> height[i];
    }
    for (int i = 0; i < man; i++)
    {
        for (int j = 0; j < man; j++)
        {
            if (weight[i] < weight[j] && height[i] < height[j]) //몸무게와 키가 더 크면 작은얘 랭킹 다운
            {
                ranking[i]++;
            }
        }
    }
    for (int i = 0; i < man; i++)
    {
        std::cout << ranking[i]+1 << " ";
    }
}