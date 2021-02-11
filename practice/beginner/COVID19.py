'''
  Problem : Coronavirus Spread
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        min_p = 100000000000
        max_p = 0
        x = 1
        for i in range(1, n):
            if a[i] - a[i - 1] <= 2:
                x += 1
            else:
                min_p = min(min_p, x)
                max_p = max(max_p, x)
                x = 1
        min_p = min(min_p, x)
        max_p = max(max_p, x)
        print('{} {}'.format(min_p, max_p))

if __name__ == '__main__':
    solve()
