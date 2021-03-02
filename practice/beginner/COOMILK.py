'''
  Problem : Bear and Milky Cookies
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 03/03/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        l = list(map(str, input().split()))
        r = 'YES'
        cookie_found = False
        for c in l:
            if c == 'cookie':
                if cookie_found == False:
                    cookie_found = True
                else:
                    r = 'NO'
            else:
                cookie_found = False
        if cookie_found:
            r = 'NO'
        print(r)

if __name__ == '__main__':
    solve()
