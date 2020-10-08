#Uses python3

import sys
def greater_or_equal(d, max_d):
    if int(str(d) + str(max_d)) >= int(str(max_d) + str(d)):
        return True
    else:
        return False

def largest_number(a):
    #write your code here
    res = ""
    while a:
        max_d = a[0]
        for d in a:
            if greater_or_equal(d, max_d):
                max_d = d
        res += str(max_d)
        a.remove(max_d)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
