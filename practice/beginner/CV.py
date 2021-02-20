'''
  Problem : Chef And Coloring
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def is_vowel(c):
    return c in ['a', 'e', 'i', 'o', 'u']

def solve():
    for _ in range(int(input())):
        n = int(input())
        s = str(input())
        r = 0
        for i in range(1, n):
            if is_vowel(s[i - 1]) == False and is_vowel(s[i]) == True:
                r += 1
        print(r)

if __name__ == '__main__':
    solve()
