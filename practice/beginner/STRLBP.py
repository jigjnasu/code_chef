'''
  Problem : Playing with Strings
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        hops = 0
        if s[0] != s[7]:
            hops += 1
        for i in range(1, 8):
            if s[i] != s[i - 1]:
                hops += 1
        if hops <= 2:
            print('uniform')
        else:
            print('non-uniform')

if __name__ == '__main__':
    solve()
