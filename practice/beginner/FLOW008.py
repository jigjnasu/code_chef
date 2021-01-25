'''
  Problem : Helping Chef
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
'''

def solve():
    for i in range(int(input())):
        n = int(input())
        if n < 10:
            print('Thanks for helping Chef!')
        else:
            print(-1)

if __name__ == '__main__':
    solve()
