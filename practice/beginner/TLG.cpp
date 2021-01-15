/*
  Problem : The Lead Game
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 16/01/2021
 */

#include <bits/stdc++.h>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int n = 0;
    std::cin >> n;
    int r = 0;
    int s = 0;
    int x = 0, y = 0;
    while(n--) {
        int a = 0, b = 0;
        std::cin >> a >> b;
        x += a; y += b;
        if (x > y && x - y > s) {
            r = 1;
            s = x - y;
        } else if (y > x && y - x > s) {
            r = 2;
            s = y - x;
        }
    }
    std::cout << r << " " << s << std::endl;

    return 0;
}
