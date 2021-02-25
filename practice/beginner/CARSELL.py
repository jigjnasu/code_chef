'''
  Problem : Football
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 25/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        p = list(map(int, input().split()))
        p.sort(reverse=True)
        laabh = 0
        for i in range(n):
            laabh += max(0, p[i] - i) % 1000000007
        print(laabh % 1000000007)

if __name__ == '__main__':
    solve()
