/*
  Problem : Reverse The Number
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 16/01/2021
 */

#include <bits/stdc++.h>

inline void swap(char& a, char& b) {
    a ^= b;
    b ^= a;
    a ^= b;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int n = 0;
    std::cin >> n;
    while (n--) {
        std::string s;
        std::cin >> s;
        int i = 0, j = s.size() - 1;
        while (i < j)
            swap(s[i++], s[j--]);
        std::cout << std::stoi(s) << std::endl;
    }

    return 0;
}
