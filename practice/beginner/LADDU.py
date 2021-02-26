'''
  Problem : Laddu
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 26/02/2021
'''

def solve():
    for _ in range(int(input())):
        n, nationality = map(str, input().split())
        points = 0
        for _ in range(int(n)):
            s = str(input())
            if s.find('WON') != -1:
                points += 300 + max(0, 20 - int(s.split()[1]))
            elif s.find('TOP') != -1:
                points += 300
            elif s.find('BUG') != -1:
                value = int(s.split()[1])
                if value >= 50 and value <= 1000:
                    points += value
            else:
                points += 50
        if nationality == 'INDIAN':
            print(points // 200)
        else:
            print(points // 400)

if __name__ == '__main__':
    solve()
