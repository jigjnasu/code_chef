'''
  Problem : Whats in the Name
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 27/02/2021
'''

def convert(s):
    r = s[0].upper()
    for i in range(1, len(s)):
        r += s[i].lower()
    return r

def solve():
    for _ in range(int(input())):
        s = str(input()).split()
        if len(s) == 1:
            print(convert(s[0]))
        else:
            for i in range(len(s) - 1):
                print(s[i][0].upper() + '.', end=' ')
            print(convert(s[len(s) - 1]))

if __name__ == '__main__':
    solve()
