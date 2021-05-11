'''
  Problem : A - Save Water Save Life
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/05/2021
'''

def solve():
    for _ in range(int(input())):
        h,x,y,c = map(int, input().split())
        if h * (x + (y // 2)) <= c:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()
