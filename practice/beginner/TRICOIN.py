'''
  Problem : Coins and Triangles
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        h = 1
        while True:
            s = (h * (h + 1)) >> 1
            if s > n:
                print(h - 1)
                break
            h += 1

if __name__ == '__main__':
    solve()
