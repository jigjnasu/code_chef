'''
  Problem : Chef and Cook-Off
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = sum(list(map(int, input().split())))
        if s == 0:
            print('Beginner')
        elif s == 1:
            print('Junior Developer')
        elif s == 2:
            print('Middle Developer')
        elif s == 3:
            print('Senior Developer')
        elif s == 4:
            print('Hacker')
        else:
            print('Jeff Dean')

if __name__ == '__main__':
    solve()
