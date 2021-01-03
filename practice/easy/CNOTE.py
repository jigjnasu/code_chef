'''
  Problem Code : CNOTE
  Problem : Chef and Notebooks
  Author : Rakesh Kumar
  Date: 03/01/2021
'''

def solve():
    t = int(input())
    for i in range(t):
        x, y, k, n = map(int, input().split())
        r = "UnluckyChef"
        for j in range(n):
            pages, prices = map(int, input().split())
            if x - y <= pages and prices <= k:
                r = "LuckyChef"
        print(r)

if __name__ == '__main__':
    solve()
