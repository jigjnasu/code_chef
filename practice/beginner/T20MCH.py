'''
  Problem : Possible Victory
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/05/2021
'''

def solve():
    r,o,s = map(int, input().split())
    if r - s < (20 - o) * 36:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    solve()
