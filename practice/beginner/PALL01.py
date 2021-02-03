'''
  Problem : The Block Game
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = str(input())
        m = ''
        for i in range(len(n) - 1, -1, -1):
            m += n[i]
        if int(n) == int(m):
            print('wins')
        else:
            print('loses')

if __name__ == '__main__':
    solve()
