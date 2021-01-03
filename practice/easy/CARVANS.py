'''
  Problem Code : CARVANS
  Problem : Carvans
  Author : Rakesh Kumar
  Date: 03/01/2021
'''

def solve():
    for i in range(int(input())):
        n = int(input())
        cars = list(map(int, input().split()))
        r = 1
        for j in range(1, n):
            if cars[j] < cars[j - 1]:
                r += 1
            else:
                cars[j] = cars[j - 1]
        print(r)

if __name__ == '__main__':
    solve()
