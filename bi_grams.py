def bi_grams(text, first, second):
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
        return result

if __name__=='__main__':
    l = 'this is a test is a text'
    print(bi_grams(l, 'is', 'a'))
    print('result should be [\'text\', \'text\']')
