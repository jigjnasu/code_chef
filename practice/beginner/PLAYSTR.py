'''
  Problem : Playing with Strings
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = str(input())
        b = str(input())
        z = 0
        o = 0
        for c in a:
            if c == '0':
                z += 1
            else:
                o += 1
        for c in b:
            if c == '0':
                z -= 1
            else:
                o -= 1
        if z == 0 and o == 0:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solve()
