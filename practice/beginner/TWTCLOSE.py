'''
  Problem : Closing the Tweets
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 12/02/2021
'''

def solve():
    n, k = map(int, input().split())
    a = [0] * 1001
    r = 0
    for _ in range(k):
        s = str(input())
        if s == 'CLOSEALL':
            a = [0] * 1001
            r = 0
        else:
            c, i = s.split()
            i = int(i)
            if a[i] == 0:
                r += 1
                a[i] = 1
            else:
                a[i] = 0
                r -= 1
        print(r)

if __name__ == '__main__':
    solve()
