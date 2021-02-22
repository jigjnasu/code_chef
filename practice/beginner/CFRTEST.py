'''
  Problem : Devu and friendship testing
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        print(len(set(list(map(int, input().split())))))

if __name__ == '__main__':
    solve()
