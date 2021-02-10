'''
  Problem : Chef and digits of a number
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        a = [0] * 2
        for c in s:
            a[ord(c) - ord('0')] += 1
        if a[0] == 1 or a[1] == 1:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()
