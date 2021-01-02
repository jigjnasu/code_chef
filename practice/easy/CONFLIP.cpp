/*
  Problem Code : JOHNY
  Problem : Uncle Johny
  Author : Rakesh Kumar
  Date: 03/01/2021
*/

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int g = 0;
        std::cin >> g;
        while (g--) {
            int s = 0, n = 0, q = 0, r = 0;
            std::cin >> s >> n >> q;
            r = n >> 1;
            if (n & 1) {
                r = n >> 1;
                if (s != q)
                    r += 1;
            }
            std::cout << r << std::endl;
        }
    }

    return 0;
}
