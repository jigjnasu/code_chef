'''
  Problem : Mutated Minions
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        r = 0
        l = list(map(int, input().split()))
        for i in l:
            if (i + k) % 7 == 0:
                r += 1
        print(r)

if __name__ == '__main__':
    solve()
