'''
  Problem : Pair Me
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 22/03/2021
'''

def solve():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        a.sort()
        if a[0] + a[1] == a[2]:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()
