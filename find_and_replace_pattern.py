# https://leetcode.com/problems/find-and-replace-pattern/

from collections import OrderedDict

def findAndReplacePattern(words, pattern):
    p = ''.join(OrderedDict.fromkeys(pattern).keys())
    
    # results list
    r = []
    
    for word in words:
        w = ''.join(OrderedDict.fromkeys(word).keys())
        
        # flag to determine if word matches pattern
        flag = True
        
        if len(w) != len(p):
            # skip this word by continuing the iteration
            continue
        
        # dict to map pattern characters to word's
        p_map = dict(zip(list(p), list(w)))
        
        # iterating through characters and checking whether they match pattern
        for i,v in enumerate(word):
            match = pattern[i]
            
            if v != p_map[match]:
                flag = False
        
        if flag:
            r.append(word)
            
    return r

if __name__ == '__main__':
    words = ['abc','deq','mee','aqq','dkd','ccc']
    pattern = 'abb'

    print(findAndReplacePattern(words, pattern))
