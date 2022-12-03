#include <iostream>

int main()
{
    int input, Checked = 0;
    std::cin >> input;
    for (int i = 0; i <= (input * 2) - 1; i++)
    {
        if (i < input)
        {
            Checked++;
        }
        else
        {
            Checked--;
        }
        for (int j = 0; j < Checked; j++)
        {
           std::cout << "*";
        }
        std::cout << "\n";
    }
}
