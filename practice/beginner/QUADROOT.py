'''
  Problem : Roots of a Quadratic Equation
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 02/03/2021
'''

import math

def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = (b * b) - (4 * a * c)
    x1 = ((-1 * b) + math.sqrt(d)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(d)) / (2 * a)
    print(x1)
    print(x2)

if __name__ == '__main__':
    solve()
