'''
  Problem : Counting Pretty Numbers
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 21/02/2021
'''

def how_many_start(c):
    if c <= 2:
        return 3
    if c <= 3:
        return 2
    if c <= 9:
        return 1

def how_many_finish(c):
    if c >= 9:
        return 3
    if c >= 3:
        return 2
    if c >= 2:
        return 1
    return 0

def solve():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        n = how_many_start(a % 10) + how_many_finish(b % 10)
        n += ((b // 10) - (a // 10) - 1) * 3
        print(n)

if __name__ == '__main__':
    solve()
