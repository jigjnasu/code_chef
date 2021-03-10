'''
  Problem : Chef and Glove
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 11/03/2021
'''

def front(ungli, dastana, n):
    r = True
    for i in range(n):
        if ungli[i] > dastana[i]:
            r = False
            break
    return r

def back(ungli, dastana, n):
    r = True
    for i in range(n):
        if ungli[i] > dastana[n - i - 1]:
            r = False
            break
    return r

def solve():
    for _ in range(int(input())):
        n = int(input())
        ungli = list(map(int, input().split()))
        dastana = list(map(int, input().split()))
        f = front(ungli, dastana, n)
        b = back(ungli, dastana, n)
        if f and b:
            print('both')
        elif f:
            print('front')
        elif b:
            print('back')
        else:
            print('none')

if __name__ == '__main__':
    solve()
