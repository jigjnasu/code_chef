'''
  Problem : Multiple Choice Exam
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 23/03/2021
'''

def solve():
    for _ in range(int(input())):
        n = int(input())
        a = str(input())
        b = str(input())
        kitna = 0
        i = 0
        while i < n:
            if a[i] == b[i]:
                kitna += 1
            elif b[i] != 'N':
                i += 1
            i += 1
        print(kitna)

if __name__ == '__main__':
    solve()
