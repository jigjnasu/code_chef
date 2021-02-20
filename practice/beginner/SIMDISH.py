'''
  Problem : Similar Dishes
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = str(input()).split()
        b = str(input()).split()
        same = 0
        for i in b:
            if i in a:
                same += 1
        if same >= 2:
            print('similar')
        else:
            print('dissimilar')

if __name__ == '__main__':
    solve()
