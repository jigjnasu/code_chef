/*
  Problem : Primality Test
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
 */

#include <bits/stdc++.h>

inline std::string is_prime(int n) {
    if (n < 2)
        return "no";
    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0)
            return "no";
    return "yes";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        std::cout << is_prime(n) << std::endl;
    }

    return 0;
}
