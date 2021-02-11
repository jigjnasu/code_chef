'''
  Problem : Candy Love
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        s = 0
        for c in a:
            s += c
        if s & 1 == 1:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()
