#Uses python3

import sys

def largest_number(a):
    #write your code here
    ans = []
    while a != []:
        max_digit = 0
        for digit in a:
            if find_safe_max(digit, max_digit):
                max_digit = digit
        ans.append(max_digit)
        a.remove(max_digit)
    return ans

def find_safe_max(digit, max_digit):
    return int(str(digit)+str(max_digit)) >= int(str(max_digit)+str(digit))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
