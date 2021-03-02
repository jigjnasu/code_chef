'''
  Problem : Bear and Ladder
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 03/03/2021
'''

def solve():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        r = 'NO'
        if abs(a - b) == 2:
            r = 'YES'
        else:
            min_v = min(a, b)
            max_v = max(a, b)
            if abs(a - b) == 1 and (min_v & 1 == 1) and (max_v & 1 == 0):
                r = 'YES'
        print(r)

if __name__ == '__main__':
    solve()
