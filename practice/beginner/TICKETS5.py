'''
  Problem : Tickets
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        if s[0] == s[1]:
            print('NO')
            return
        for i in range(len(s)):
            if i & 1:
                if s[i] != s[1]:
                    print('NO')
                    return
            else:
                if s[i] != s[0]:
                    print('NO')
                    return
        print('YES')


if __name__ == '__main__':
    solve()
