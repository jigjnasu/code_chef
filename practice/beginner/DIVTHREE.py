'''
  Problem : Chef and Division 3
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 28/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, k, d = map(int, input().split())
        print(min(sum(list(map(int, input().split()))) // k, d))

if __name__ == '__main__':
    solve()

