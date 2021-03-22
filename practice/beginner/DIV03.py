'''
  Problem : Daanish and Problems
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/03/2021
'''

def solve():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        k = int(input())
        for i in range(9, -1, -1):
            if k >= a[i]:
                k -= a[i]
            elif a[i] == 0:
                continue
            else:
                print(i + 1)
                break

if __name__ == '__main__':
    solve()
