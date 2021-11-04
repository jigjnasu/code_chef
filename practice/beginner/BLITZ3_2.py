'''
  Problem : Chess Match
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/11/2021
'''

def solve():
    for i in range(int(input())):
        a = [int(x) for x in input().split()]
        print((2 * (180 + a[0])) - (a[1] + a[2]))

if __name__ == '__main__':
    solve()