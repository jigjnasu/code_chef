'''
  Problem : Chef and Two Strings
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = str(input())
        b = str(input())
        min_d = 0
        max_d = 0
        for i in range(len(a)):
            if a[i] == '?' and b[i] == '?':
                max_d += 1
            elif a[i] == '?' or b[i] == '?':
                max_d += 1
            elif a[i] != b[i]:
                min_d += 1
                max_d += 1
        print('{} {}'.format(min_d, max_d))

if __name__ == '__main__':
    solve()
