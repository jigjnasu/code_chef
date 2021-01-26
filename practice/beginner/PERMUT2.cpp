/*
  Problem : Ambiguous Permutations
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
*/

#include <bits/stdc++.h>

inline std::string perm(int n) {
    int e = 0;
    std::cin >> e;
    if (n != e)
        return "not ambiguous";

    for (int i = 1; i < n; ++i) {
        std::cin >> e;
        if (i != e)
            return "not ambiguous";
    }
    return "ambiguous";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    while (1) {
        int n = 0;
        std::cin >> n;

        if (n == 0)
            break;
        std::cout << perm(n) << std::endl;
    }

    return 0;
}
