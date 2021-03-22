'''
  Problem : Chef Diet
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 22/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        r = 'YES'
        d = 0
        s = 0
        p = list(map(int, input().split()))
        for i in range(n):
            if s + p[i] < k:
                r = 'NO'
                d = i + 1
                break
            else:
                if p[i] >= k:
                    s += p[i] - k
                else:
                    s -= k - p[i]
        if r == 'YES':
            print(r)
        else:
            print('NO', d)

if __name__ == '__main__':
    solve()
