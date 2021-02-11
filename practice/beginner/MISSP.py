'''
  Problem : Chef and Two Strings
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = [0] * 100001
        n = int(input())
        for _ in range(n):
            e = int(input())
            a[e] += 1
        for i in range(len(a)):
            if a[i] & 1:
                print(i)

if __name__ == '__main__':
    solve()
