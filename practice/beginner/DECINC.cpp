/*
  Problem Code : DECINC
  Problem : Decrement OR Increment
  Author : Rakesh Kumar
  Date: 25/08/2020
*/

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int n = 0;
    std::cin >> n;
    if (n % 4 == 0)
        std::cout << n + 1 << std::endl;
    else
        std::cout << n - 1 << std::endl;

    return 0;
}
