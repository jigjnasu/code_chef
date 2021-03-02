'''
  Problem : Good and Bad Persons
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 02/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = str(input())
        arr = [0] * 2
        for c in s:
            if c.isupper():
                arr[1] += 1
            else:
                arr[0] += 1
        if arr[0] + k < n and arr[1] + k < n:
            print('none')
        elif arr[0] + k >= n and arr[1] + k >= n:
            print('both')
        elif arr[0] + k >= n:
            print('chef')
        else:
            print('brother')

if __name__ == '__main__':
    solve()
