# Python3

a, b = [int(i) for i in input().split()]

def lcm_test(a, b):
    if b == 0:
        return a
    c = a%b
    return lcm_test(b, c)

if a>b:
    lcm = lcm_test(a, b)
else:
    lcm = lcm_test(b, a)

print(a*b//lcm)