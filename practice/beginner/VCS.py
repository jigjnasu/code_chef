'''
  Problem : Version Control System
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        ignored = list(map(int, input().split()))
        tracked = list(map(int, input().split()))

        x = 0
        y = 0
        for i in range(1, n + 1):
            if i in ignored and i in tracked:
                x += 1
            if i not in ignored and i not in tracked:
                y += 1
        print('{} {}'.format(x, y))

if __name__ == '__main__':
    solve()
