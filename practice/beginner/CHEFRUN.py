'''
  Problem : Secret Recipe
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        t1 = abs(a[2] - a[0]) / a[3]
        t2 = abs(a[2] - a[1]) / a[4]
        if t1 > t2:
            print('Kefa')
        elif t1 < t2:
            print('Chef')
        else:
            print('Draw')

if __name__ == '__main__':
    solve()
