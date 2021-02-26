'''
  Problem : From heaven to earth
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/02/2021
'''

import math

def solve():
    for _ in range(int(input())):
        n, v1, v2 = map(int, input().split())
        t1 = n / v1
        t2 = (math.sqrt(2) * n) / v2
        if t1 < t2:
            print('Stairs')
        else:
            print('Elevator')

if __name__ == '__main__':
    solve()
