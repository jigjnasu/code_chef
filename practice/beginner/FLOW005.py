'''
  Problem : Smallest Numbers of Notes
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 24/02/2021
'''

def paisa(n):
    c = 0
    for note in [100, 50, 10, 5, 2, 1]:
        while note <= n:
            c += 1
            n -= note
    return c

def solve():
    for _ in range(int(input())):
        n = int(input())
        print(paisa(n))

if __name__ == '__main__':
    solve()
