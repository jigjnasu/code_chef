'''
  Problem : Malvika is peculiar about color of balloons
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        a = [0] * 2
        for c in s:
            a[ord(c) - ord('a')] += 1
        print(min(a[0], a[1]))

if __name__ == '__main__':
    solve()


