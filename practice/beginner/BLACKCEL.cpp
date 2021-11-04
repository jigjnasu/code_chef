/*
  Problem : Black cells in a chessboard
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/11/2021
 */

#include <bits/stdc++.h>

using ll = unsigned long long int;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    ll n = 0;
    std::cin >> n;
    std::cout << ((n * n) >> 1) << std::endl;

    return 0;
}