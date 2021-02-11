'''
  Problem : ATM Machine
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        res = ''
        a = list(map(int, input().split()))
        for m in a:
            if k >= m:
                res += '1'
                k -= m
            else:
                res += '0'
        print(res)

if __name__ == '__main__':
    solve()
