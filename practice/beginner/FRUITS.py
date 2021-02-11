'''
  Problem : Chef and Fruits
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        d = abs(n - m)
        print(max(0, d - k))

if __name__ == '__main__':
    solve()
