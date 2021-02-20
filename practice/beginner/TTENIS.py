'''
  Problem : Chef and Table Tennis
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        vijay = 0
        for p in s:
            vijay += int(p)
        parajay = len(s) - vijay
        res = 'LOSE'
        if vijay >= 11:
            if parajay < 10:
                res = 'WIN'
            if vijay - parajay >= 2:
                res = 'WIN'
        print(res)

if __name__ == '__main__':
    solve()
