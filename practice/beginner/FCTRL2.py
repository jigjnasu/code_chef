'''
  Problem : Small factorials
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 17/01/2021
'''

def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f)

if __name__ == '__main__':
    for i in range(int(input())):
        fact(int(input()))
