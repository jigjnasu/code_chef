'''
  Problem : Cutting Recipes
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 07/02/2021
'''

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def solve():
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        r = arr[1]
        for i in range(2, arr[0] + 1):
            r = gcd(r, arr[i])
        for i in range(1, arr[0] + 1):
            print(arr[i] // r, end=' ')
        print()

if __name__ == '__main__':
    solve()
