'''
  Problem : Chef and Rainbow Array
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = a.copy()
        b.reverse()
        r = 'yes'
        if a != b:
            r = 'no'
        if set(a) != {1, 2, 3, 4, 5, 6, 7}:
            r = 'no'
        print(r)

if __name__ == '__main__':
    solve()
