#include <iostream>

int num[1000001], count = 9, number, max = -10000001;

int main(void)
{
    
    for (int i = 0; i < count; i++)
    {
        std::cin >> num[i];
        if (i == 0)
        {
            max = num[i];
            number = i + 1;
        }
        else
        {
            if (num[i] > max)
            {
                max = num[i];
                number = i + 1;
            }
        }
    }
    std::cout << max << "\n" << number;
}
