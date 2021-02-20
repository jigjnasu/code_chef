'''
  Problem : Sed Sequences
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 21/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if sum(list(map(int, input().split()))) % k == 0:
            print(0)
        else:
            print(1)

if __name__ == '__main__':
    solve()
