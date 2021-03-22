'''
  Problem : Highest Divisor
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/03/2021
'''

def solve():
    n = int(input())
    for i in range(10, 0, -1):
        if n % i == 0:
            print(i)
            break

if __name__ == '__main__':
    solve()
