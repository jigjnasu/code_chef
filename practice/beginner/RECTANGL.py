'''
  Problem : Rectangle
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 27/01/2021
'''

def solve():
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        arr.sort()
        if arr[0] == arr[1] and arr[2] == arr[3]:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()
