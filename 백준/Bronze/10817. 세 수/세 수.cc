
#include <iostream>

int main()
{
    int a, b, c, mid_mum;
    std::cin >> a >> b >> c;
    if(a >= b && a >= c) // a가 제일 클때
        if (b >= c)
        {
            std::cout << b;
            return 0;
        }
        else
        {
            std::cout << c;
            return 0;

        }
    if (b >= a && b >= c) // a가 제일 클때
        if (a >= c)
        {
            std::cout << a;
            return 0;

        }
        else
        {
            std::cout << c;
            return 0;

        }
    if (c >= b && c >= a) // a가 제일 클때
        if (b >= a)
        {
            std::cout << b;
            return 0;

        }
        else
        {
            std::cout << a;
            return 0;

        }
}