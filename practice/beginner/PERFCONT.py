'''
  Problem : A Balanced Contest
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        p, n = map(int, input().split())
        a = list(map(int, input().split()))

        easy = 0
        hard = 0
        for x in a:
            if x / n >= 0.50:
                easy += 1
            if x / n <= 0.10:
                hard += 1
        if easy == 1 and hard == 2:
            print('yes')
        else:
            print('no')

if __name__ == '__main__':
    solve()
