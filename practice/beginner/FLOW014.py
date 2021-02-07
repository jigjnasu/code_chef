'''
  Problem : Grade The Steel
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 08/02/2021
'''

def conds(h, c, t):
    cnt = []
    if h > 50:
        cnt.append(1)
    if c < 0.7:
        cnt.append(2)
    if t > 5600:
        cnt.append(3)
    return cnt

def solve():
    for _ in range(int(input())):
        h, c, t = map(str, input().split())
        h = int(h)
        c = float(c)
        t = int(t)
        cnt = conds(h, c, t)
        if len(cnt) == 3:
            print(10)
        elif 1 in cnt and 2 in cnt:
            print(9)
        elif 2 in cnt and 3 in cnt:
            print(8)
        elif 1 in cnt and 3 in cnt:
            print(7)
        elif len(cnt) == 1:
            print(6)
        else:
            print(5)

if __name__ == '__main__':
    solve()
