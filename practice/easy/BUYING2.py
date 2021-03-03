'''
  Problem : Buying Sweets
  Author : Rakesh Kumar
  Date: 03/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        s = sum(arr)
        if s % x >= min(arr):
            print(-1)
        else:
            print(s // x)

if __name__ == '__main__':
    solve()
