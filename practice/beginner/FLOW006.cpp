/*
  Problem Code : FLOW006
  Problem : Sum of Digits
  Author : Rakesh Kumar
  Date: 02/02/2021
*/

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        std::string n;
        std::cin >> n;

        int s = 0;
        for (char c : n)
            s += c - '0';
        std::cout << s << std::endl;
    }

    return 0;
}
