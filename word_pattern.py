def wordPattern(pattern, s):
    matching = {}
    pattern = list(pattern)
    s = s.split(' ')

    for i,p in enumerate(pattern):
        print('Matching: {}', matching)
        try:
           if s[i] != matching[p]:
               return False
        except KeyError:
            matching[p] = s[i]
    return True
           

if __name__=='__main__':
    print(wordPattern('abba', 'dog cat cat dog'))
    print(wordPattern('abba', 'dog cat cat fish'))
    print(wordPattern('aaaa', 'dog cat cat fish'))
    print(wordPattern('abba', 'dog dog dog dog'))
