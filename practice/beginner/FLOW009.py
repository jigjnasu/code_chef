'''
  Problem : Total Expenses
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
'''

def solve():
    for _ in range(int(input())):
        n, p = map(int, input().split())
        t = n * p
        if n > 1000:
            t -= t * 0.10
        print(t)

if __name__ == '__main__':
    solve()
