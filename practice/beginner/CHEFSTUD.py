'''
  Problem : Chef and his Students
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def solve():
    for _ in range(int(input())):
        s = str(input())
        r = ''
        for c in s:
            if c == '>':
                r += '<'
            elif c == '<':
                r += '>'
            else:
                r += c
        dhunai = 0
        for i in range(1, len(r)):
            if r[i - 1] == '>' and r[i] == '<':
                dhunai += 1
        print(dhunai)

if __name__ == '__main__':
    solve()
