'''
  Problem : Mix the Colors
  Author : Rakesh Kumar
  Date: 03/03/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        d = {}
        f = 0
        for a in arr:
            if a in d:
                f += 1
            else:
                d[a] = True
        print(f)

if __name__ == '__main__':
    solve()
