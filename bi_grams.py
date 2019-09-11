# https://leetcode.com/problems/occurrences-after-bigram/
# Passed: 16ms, 11.8MB


def bi_grams(text, first, second):
    # To keep track of seen grams
    flag_first_gram = False
    flag_second_gram = False
    
    result = []
    
    for word in text.split(' '):
        if flag_first_gram and flag_second_gram:
            result.append(word)
            flag_first_gram = flag_second_gram = False
            
            
        if word == first:
            flag_first_gram = True
        elif flag_first_gram and word == second:
            flag_second_gram = True
        elif word != first and word != second:
            flag_first_gram = flag_second_gram = False
    return result
if __name__=='__main__':
    l = 'this is a test is a text'
    print(bi_grams(l, 'is', 'a'))
    print('result should be [\'text\', \'text\']')
