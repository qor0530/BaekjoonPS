#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
int main()
{
    int ham[3], drink[2], low_ham = 0, low_drink = 0, set;
    std::cin >> ham[0];
    std::cin >> ham[1];
    std::cin >> ham[2];
    std::cin >> drink[0];
    std::cin >> drink[1];
    low_ham = std::min({ ham[0], ham[1], ham[2] });
    low_drink = std::min({drink[0], drink[1]});
    set = low_drink + low_ham - 50;
    std::cout << set;
}
