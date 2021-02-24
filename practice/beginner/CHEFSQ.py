'''
  Problem : Chef and his Sequence
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 24/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        b = list(map(int, input().split()))
        c = 0
        for i in range(n):
            if a[i] == b[c]:
                c += 1
            if c == m:
                break
        if c == m:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()
