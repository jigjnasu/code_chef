'''
  Problem : A Good Set
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 03/03/2021
'''

def solve():
    for _ in range(int(input())):
        i = 1
        for _ in range(int(input())):
            print(i, end=' ')
            i += 2
        print()

if __name__ == '__main__':
    solve()
