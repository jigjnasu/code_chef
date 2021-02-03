'''
  Problem : Id and Ship
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 04/02/2021
'''

def solve():
    for _ in range(int(input())):
        c = str(input())
        if c.lower() == 'b':
            print('BattleShip')
        elif c.lower() == 'c':
            print('Cruiser')
        elif c.lower() == 'd':
            print('Destroyer')
        elif c.lower() == 'f':
            print('Frigate')

if __name__ == '__main__':
    solve()
