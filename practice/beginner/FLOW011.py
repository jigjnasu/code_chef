'''
  Problem : Gross Salary
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/01/2021
'''

def solve():
    for _ in range(int(input())):
        aay = int(input())
        atirikt_aay = 0
        if aay < 1500:
            atirikt_aay += aay * 0.10 + aay * 0.90
        else:
            atirikt_aay += 500 + aay * 0.98
        print(atirikt_aay + aay)

if __name__ == '__main__':
    solve()
