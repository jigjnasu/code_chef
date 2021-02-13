'''
  Problem : Cops and the Thief Devu
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        m, x, y = map(int, input().split())
        kunba = [1] * 100
        cops = list(map(int, input().split()))
        for c in cops:
            s = max(1, c - x * y)
            e = min(100, c + x * y)
            for i in range(s, e + 1):
                kunba[i - 1] = 0
        print(sum(kunba))

if __name__ == '__main__':
    solve()
