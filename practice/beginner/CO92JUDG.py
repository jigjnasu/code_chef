'''
  Problem : Chef Judges a Competition
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a = sum(a) - max(a)
        b = sum(b) - max(b)
        if a < b:
            print('Alice')
        elif b < a:
            print('Bob')
        else:
            print('Draw')

if __name__ == '__main__':
    solve()
