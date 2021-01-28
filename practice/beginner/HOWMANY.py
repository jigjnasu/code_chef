'''
  Problem : how many digits do I have
  Author @ Rakesh Kumar
  cpp.rakesh@gmail.com
  Date : 29/01/2021
'''

if __name__ == '__main__':
    n = len(str(input()))
    if n > 3:
        print('More than 3 digits')
    else:
        print(n)
