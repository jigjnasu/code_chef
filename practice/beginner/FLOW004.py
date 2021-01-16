'''
  Problem : First and Last Digit
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 17/01/2021
'''

def solve(n):
    f = ord(n[0]) - ord('0')
    l = ord(n[len(n) - 1]) - ord('0')
    print(f + l)

if __name__ == '__main__':
    for i in range(int(input())):
        solve(str(input()))
