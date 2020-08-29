/*
  Problem : Find Your Gift
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/08/2020
 */

#include <bits/stdc++.h>

inline void move(char i, int& x, int& y) {
    switch (i) {
    case 'L': --x; break;
    case 'R': ++x; break;
    case 'U': ++y; break;
    case 'D': --y; break;
    default:       break;
    }
}

inline int where(char i) {
    int axis = 0;
    if (i == 'U' || i == 'D')
        axis = 1;
    return axis;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0); std::cout.tie(0);

    int t = 0;
    std::cin >> t;
    while (t--) {
        int n = 0;
        std::cin >> n;
        char p = ' ';
        std::cin >> p; --n;
        int x = 0, y = 0, axis = where(p);
        move(p, x, y);
        while (n--) {
            char i;
            std::cin >> i;
            if (axis != where(i))
                move(i, x, y);
            axis = where(i);
            p = i;
        }
        std::cout << x << " " << y << std::endl;
    }

    return 0;
}
