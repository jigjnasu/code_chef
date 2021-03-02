'''
  Problem : Devu and Grapes
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 02/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        total = 0
        for a in arr:
            r = a % k
            if a >= k:
                total += min(r, k - r)
            else:
                total += k - r
        print(total)

if __name__ == '__main__':
    solve()
