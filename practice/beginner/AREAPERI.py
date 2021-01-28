'''
  Problem : Area OR Perimeter
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 29/01/2021
'''

def solve():
    l = int(input())
    b = int(input())
    a = l * b
    p = 2 * (l + b)
    if a > p:
        print('Area')
        print(a)
    elif p > a:
        print('Peri')
        print(p)
    else:
        print('Eq')
        print(a)

if __name__ == '__main__':
    solve()
