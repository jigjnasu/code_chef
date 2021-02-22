'''
  Problem : Cats and Dogs
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        c, d, l = map(int, input().split())
        x = l // 4
        m = d + max(0, c - (d << 1))
        r = 'yes'
        if l % 4 != 0:
            r = 'no'
        if not (x >= m and x <= c + d):
            r = 'no'
        print(r)


if __name__ == '__main__':
    solve()
