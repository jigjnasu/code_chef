'''
  Problem : Lost Weekends
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 27/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        s = 0
        for i in range(5):
            s += a[i] * a[5]
        if s <= 120:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    solve()
