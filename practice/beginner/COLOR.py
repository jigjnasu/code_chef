'''
  Problem : Chef And Coloring
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 20/02/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        satrangi = str(input())
        dict = {'R' : 0, 'G' : 0, 'B' : 0}
        rang_max = 0
        for c in satrangi:
            dict[c] = dict[c] + 1
            rang_max = max(rang_max, dict[c])
        print(n - rang_max)

if __name__ == '__main__':
    solve()
