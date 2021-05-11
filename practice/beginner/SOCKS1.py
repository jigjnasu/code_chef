'''
  Problem : Valid Pair
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/05/2021
'''

def solve():
    a, b, c = map(int, input().split())
    if a == b or a == c or b == c:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    solve()
