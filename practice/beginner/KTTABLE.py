'''
  Problem : Kitchen Timetable
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        t = list(map(int, input().split()))
        r = list(map(int, input().split()))
        res = 0
        if r[0] <= t[0]:
            res += 1
        for i in range(1, n):
            if r[i] <= t[i] - t[i - 1]:
                res += 1
        print(res)

if __name__ == '__main__':
    solve()
