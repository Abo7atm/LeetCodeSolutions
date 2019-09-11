# https://leetcode.com/problems/valid-parentheses/
# Passed: 40ms, 13.8MB
           
def is_valid(s: str) -> bool:
    pairs = {'(': ')', '{': '}', '[': ']'}
    opening = list(pairs.keys())

    nxt = []

    for i in s:
        if i in opening:
            nxt.insert(0, pairs[i])
        else:
            if len(nxt) == 0:
                return False
            if nxt.pop(0) != i:
                return False
    if len(nxt) == 0:
        return True
    return False

if __name__=='__main__':
    while True:
        s = input('enter set of paran: (x to exit) ')
        if s == 'x':
            break
        print(is_valid(s))
