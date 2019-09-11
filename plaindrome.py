# https://leetcode.com/problems/palindrome-number/
# Passed: 72ms, 14MB

def isPalindrome(self, x: int) -> bool:
    x = str(x)
    if len(x) == 0:
        return True
    for i,v in enumerate(x):
        if x[i] != x[len(x)-i-1]:
            return False
        
    return True