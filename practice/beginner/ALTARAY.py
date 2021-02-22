'''
  Problem : Alternating subarray prefix
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        r = [1] * n
        for i in range(n - 2, -1, -1):
            if a[i] >= 0 and a[i + 1] < 0:
                r[i] = r[i + 1] + 1
            if a[i] < 0 and a[i + 1] >= 0:
                r[i] = r[i + 1] + 1
        for e in r:
            print(e, end=' ')
        print()

if __name__ == '__main__':
    solve()
