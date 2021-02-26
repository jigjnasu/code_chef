'''
  Problem : Snake Procession
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 25/02/2021
'''

B = ['H', 'T']

def solve():
    for _ in range(int(input())):
        n = int(input())
        s = str(input())
        t = ''
        for c in s:
            if c != '.':
                t += c
        r = 'Valid'
        if len(t) % 2 == 1:
            r = 'Invalid'
        else:
            for i in range(len(t)):
                if B[i % 2] != t[i]:
                    r = 'Invalid'
                    break
        print(r)

if __name__ == '__main__':
    solve()
