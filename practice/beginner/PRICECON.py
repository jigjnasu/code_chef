'''
  Problem : Chef and Price Control
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        s = 0
        for p in arr:
            s += max(0, p - k)
        print(s)

if __name__ == '__main__':
    solve()
