'''
  Problem : Id and Ship
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
'''

def solve():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(max(0, x - y))

if __name__ == '__main__':
    solve()
