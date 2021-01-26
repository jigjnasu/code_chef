/*
  Problem : Farmer Feb
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
*/

#include <bits/stdc++.h>

inline bool is_prime(int n) {
    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0)
            return false;
    return true;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int a = 0, b = 0;
        std::cin >> a >> b;

        int s = a + b + 1;
        while (!is_prime(s))
            ++s;
        std::cout << s - (a + b) << std::endl;
    }

    return 0;
}

