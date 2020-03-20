# Uses python3
import sys

def optimal_summands(n):
    summands = []
    n1 = n
    for i in range(1,n+1):
        if n1 == 0:
            summands.append(i)
            break
        elif n1 <= i:
            summands.append(n1+i)
            break
        else:
            summands.append(i)
            
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
