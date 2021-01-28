'''
  Problem : Mahasena
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 29/01/2021
'''

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    o = 0
    e = 0
    for a in arr:
        if a & 1 == 1:
            o += 1
        else:
            e += 1
    if e > o:
        print('READY FOR BATTLE')
    else:
        print('NOT READY')

if __name__ == '__main__':
    solve()
