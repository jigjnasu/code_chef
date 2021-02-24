'''
  Problem : Bear and Segment 01
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 25/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        cnt = s.count('1')
        r = 'YES'
        if cnt == 0:
            r = 'NO'
        else:
            i = s.index('1')
            j = s.rindex('1')
            if j - i + 1 != cnt:
                r = 'NO'
        print(r)

if __name__ == '__main__':
    solve()
