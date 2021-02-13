'''
  Problem : Chef and the Wildcard Matching
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 14/02/2021
'''

def solve():
    for _ in range(int(input())):
        a = str(input())
        b = str(input())
        res = 'Yes'
        for i in range(len(a)):
            if not (a[i] == '?' or b[i] == '?'):
                if a[i] != b[i]:
                    res = 'No'
                    break
        print(res)

if __name__ == '__main__':
    solve()
