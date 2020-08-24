/*
  Problem Code : CHOPRT
  Problem : Chef And Operators
  Author : Rakesh Kumar
  Date: 25/08/2020
*/

#include <bits/stdc++.h>

using ull = unsigned long long int;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        ull a = 0, b = 0;
        std::cin >> a >> b;
        if (a > b)
            std::cout << ">" << std::endl;
        else if (a < b)
            std::cout << "<" << std::endl;
        else
            std::cout << "=" << std::endl;
    }

    return 0;
}
