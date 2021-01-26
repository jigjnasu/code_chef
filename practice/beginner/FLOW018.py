'''
  Problem : Small Factorial
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
'''

def fac():
    f = [1, 1]
    for i in range(2, 22):
        f.append(f[i - 1] * i)
    return f

if __name__ == '__main__':
    f = fac()
    for i in range(int(input())):
        n = int(input())
        print(f[n])
