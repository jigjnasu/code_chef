'''
  Problem : Buying New Tablet
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, b = map(int, input().split())
        max_area = 0
        for _ in range(n):
            w, h, p = map(int, input().split())
            if p <= b:
                max_area = max(max_area, w * h)
        if max_area:
            print(max_area)
        else:
            print('no tablet')

if __name__ == '__main__':
    solve()
