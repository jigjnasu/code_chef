'''
  Problem : Cool Name
  Author : Rakesh Kumar
  Date: 07/11/2021
'''

def solve():
    for _ in range(int(input())):
      s = sorted(str(input()))
      r = 0
      for i in range(len(s)):
        r += (i + 1) * ((ord(s[i]) - ord('a')) + 1)
      print(r)

if __name__ == '__main__':
    solve()