'''
  Problem : Find the Maximum Value
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        a.sort()
        if len(a) - 1 == a[-1]:
            print(a[-2])
        else:
            print(a[-1])

if __name__ == '__main__':
    solve()
