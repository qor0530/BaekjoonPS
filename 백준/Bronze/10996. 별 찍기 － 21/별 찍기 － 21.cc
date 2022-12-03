#include <iostream>

int main()
{
    int input, Check = 0;
    std::cin >> input;
    for (int i = 1; i <= input * 2; i++)
    {
        if (i % 2 == 0)
        {
            Check = 1;
        }
        else
        {
            Check = 0;
        }
        for (int j = 0; j < input; j++)
        {
            if (j % 2 == Check)
            {
                std::cout << "*";
            }
            else
            {
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }
}
