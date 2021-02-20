'''
  Problem : Simple Statistics
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        if k > 0:
            arr.sort()
            arr = arr[k:]
            arr = arr[:-k]
            print(sum(arr) / (n - (k << 1)))
        else:
            print(sum(arr) / n)

if __name__ == '__main__':
    solve()
