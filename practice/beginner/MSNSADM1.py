'''
  Problem : Football
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 25/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        m = 0
        for i in range(n):
            m = max(m, a[i] * 20 - b[i] * 10)
        print(m)

if __name__ == '__main__':
    solve()
