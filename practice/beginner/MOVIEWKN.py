'''
  Problem : Movie Weekend
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        res = 0
        max_t = 0
        max_r = 0
        for i in range(n):
            if l[i] * r[i] >= max_t and r[i] > max_r:
                max_t = l[i] * r[i]
                max_r = r[i]
                res = i + 1
        print(res)

if __name__ == '__main__':
    solve()
