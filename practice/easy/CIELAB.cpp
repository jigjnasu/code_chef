/*
  Problem Code : CIELAB
  Problem : Ciel and A-B Problem
  Author : Rakesh Kumar
  Date: 02/02/2021
*/

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int a = 0, b = 0;
    std::cin >> a >> b;
    std::string r = std::to_string(a - b);
    if (r[0] == '9')
        r[0] = '1';
    else
        r[0] = r[0] + 1;
    std::cout << r << std::endl;

    return 0;
}
