'''
  Problem : Studying Alphabet
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/02/2021
'''

def solve():
    phada_likha = str(input())
    for _ in range(int(input())):
        s = str(input())
        r = 'Yes'
        for c in s:
            if c not in phada_likha:
                r = 'No'
                break
        print(r)

if __name__ == '__main__':
    solve()
