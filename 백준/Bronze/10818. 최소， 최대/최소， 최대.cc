#include <iostream>

int main(void)
{
    int num[1000001], count, min = 10000001, max = -10000001;
    std::cin >> count;

    for (int i = 0; i < count; i++)
    {
        std::cin >> num[i];
        if (i == 0)
        {
            min = num[i];
            max = num[i];
        }
        else
        {
            if (num[i] > max)
            {
                max = num[i];
            }
            if (num[i] < min)
            {
                min = num[i];
            }
        }
    }
    std::cout << min << " " << max;
}
