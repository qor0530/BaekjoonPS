#include <iostream>

int main()
{
    int test[5], aver = 0;
    for(int i = 0; i < 5; i++)
    {
        std::cin >> test[i];
        if (test[i] < 40)
        {
            test[i] = 40;
        }
        aver = aver + test[i];
    }
    std::cout << aver / 5;
}
