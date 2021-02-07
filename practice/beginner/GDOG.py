'''
  Problem : Greedy puppy
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 08/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        uttam_maal = 0
        for i in range(1, k + 1):
            uttam_maal = max(uttam_maal, n % i)
        print(uttam_maal)

if __name__ == '__main__':
    solve()
