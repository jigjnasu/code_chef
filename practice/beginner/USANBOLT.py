'''
  Problem : Usain Bolt vs Tiger
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 21/02/2021
'''

import math

def solve():
    for _ in range(int(input())):
        f, db, ta, bs = map(int, input().split())
        bolt = f / bs
        tiger = math.sqrt(((f + db) << 1) / ta)
        if bolt < tiger:
            print('Bolt')
        else:
            print('Tiger')

if __name__ == '__main__':
    solve()
