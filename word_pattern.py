# https://leetcode.com/problems/word-pattern/
# Passed: 40ms, 13.9MB

def wordPattern(pattern, s):
    s = s.split(' ')

    # remove all whitespaces
    pattern = pattern.replace(' ', '')

    # check if there are more 'patterns' than words
    if len(set(s)) != len(set(list(pattern))):
        return False

    # Word => pattern char
    matching = dict(set(zip(s, pattern)))
    print('Matching: {}'.format(matching))
    
    for idx, word in enumerate(s):
        if matching[word] != pattern[idx]:
            return False

    return True


if __name__=='__main__':
    print(wordPattern('abba', 'dog cat cat dog'))
    print(wordPattern('abba', 'dog cat cat fish'))
    print(wordPattern('aaaa', 'dog cat cat fish'))
    print(wordPattern('abba', 'dog dog dog dog'))
