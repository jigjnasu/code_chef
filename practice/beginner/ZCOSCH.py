'''
  Problem : How much Scholarship
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 01/02/2021
'''

def solve():
    rank = int(input())
    if rank >= 1 and rank <= 50:
        print(100)
    elif rank >= 51 and rank <= 100:
        print(50)
    else:
        print(0)

if __name__ == '__main__':
    solve()
