'''
  Problem : Medel
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 30/03/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        min_n, max_n = min(a), max(a)
        for v in a:
            if v == min_n:
                print(v, end=' ')
            elif v == max_n:
                print(v, end=' ')
        print()

if __name__ == '__main__':
    solve()
