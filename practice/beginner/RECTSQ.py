'''
  Problem : Farmer And His Plot
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def solve():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = gcd(n, m)
        print((n * m) // (g * g))

if __name__ == '__main__':
    solve()
