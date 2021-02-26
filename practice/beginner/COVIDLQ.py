'''
  Problem : COVID Pandemic and Long Queue
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        r = 'YES'
        last = -1
        for i in range(n):
            if a[i] == 1:
                if last == -1:
                    last = i
                else:
                    if i - last < 6:
                        r = 'NO'
                        break
                    last = i
        print(r)

if __name__ == '__main__':
    solve()
