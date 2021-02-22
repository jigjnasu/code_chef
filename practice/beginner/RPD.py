'''
  Problem : Easy Math
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def digit_sum(a, b):
    n = str(a * b)
    r = 0
    for c in n:
        r += ord(c) - ord('0')
    return r

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        r = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                r = max(r, digit_sum(a[i], a[j]))
        print(r)

if __name__ == '__main__':
    solve()
