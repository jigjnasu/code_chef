'''
  Problem : Dinosaurs Football
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/03/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a=[]
        for i in range(n, 0, -1):
            a.append(i)
        a[0:k+1]=reversed(a[0:k+1])
        print(*a)

if __name__ == '__main__':
    solve()
