'''
  Problem : Tanu and Head-bob
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 08/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        s = str(input())
        if 'I' in s:
            print('INDIAN')
        elif 'Y' in s:
            print('NOT INDIAN')
        else:
            print('NOT SURE')

if __name__ == '__main__':
    solve()
