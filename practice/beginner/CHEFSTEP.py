'''
  Problem : Chef and Steps
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        for d in a:
            if d % k == 0:
                print('1', end='')
            else:
                print('0', end='')
        print()

if __name__ == '__main__':
    solve()
