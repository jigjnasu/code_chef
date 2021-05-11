'''
  Problem : Coldplay
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/05/2021
'''

def solve():
    for _ in range(int(input())):
        m, s = map(int, input().split())
        print(m // s)

if __name__ == '__main__':
    solve()
