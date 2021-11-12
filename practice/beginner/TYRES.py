'''
  Problem : Cars and Bikes
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/11/2021
'''

def solve():
    for _ in range(int(input())):
        if int(input()) % 4 == 0:
            print('NO')
        else:
            print('YES')

if __name__ == '__main__':
    solve()