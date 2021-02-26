'''
  Problem : That Is My Score!
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        ank_talika = [0] * 8
        for _ in range(n):
            p, s = map(int, input().split())
            if p < 9:
                ank_talika[p - 1] = max(ank_talika[p - 1], s)
        print(sum(ank_talika))

if __name__ == '__main__':
    solve()
