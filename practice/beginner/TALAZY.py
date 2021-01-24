'''
  Problem : Lazy Jem
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 24/01/2021
'''

import math

def solve(n, b, m):
    r = 0
    while True:
        t = math.ceil(n / 2)
        r += t * m
        n -= t
        if (n <= 0):
            break
        r += b
        m = m << 1
    return r

if __name__ == '__main__':
    for i in range(int(input())):
        n, b, m = map(int, input().split())
        print(solve(n, b, m))

