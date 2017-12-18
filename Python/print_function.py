# print all the numbers until a certain number

from __future__ import print_function
if __name__ == '__main__':
    i = 1
    n = int(raw_input())
    
    while (i <= n):
        print(i, end = ''),
        i += 1
