/*
  Problem : Two Numbers
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int a = 0, b = 0, n = 0;
        std::cin >> a >> b >> n;
        if (n & 1)
            a <<= 1;
        if (a > b)
            std::cout << a / b << std::endl;
        else
            std::cout << b / a << std::endl;
    }

    return 0;
}
