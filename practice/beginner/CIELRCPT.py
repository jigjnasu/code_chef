'''
  Problem : Ciel and Receipt
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
'''

def solve():
    d = []
    for i in range(11, -1, -1):
        d.append(1 << i)

    for _ in range(int(input())):
        n = int(input())
        t = 0
        for i in range(len(d)):
            t += n // d[i]
            n = n % d[i]
        print(t)

if __name__ == '__main__':
    solve()
