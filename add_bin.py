def add_binary(a: str, b:str) -> str:
    a='0b'+a
    b='0b'+b
    return bin(int(a,2)+int(b,2))[2:]

if __name__=='__main__':
    flag = True
    while flag:
        user_input = input('enter two binary numbers separated by space: (x to exit) ')

        if user_input == 'x':
            flag = False
            continue

        i = user_input.split(' ')
        a = i[0]
        b = i[1]

        print('result: {}'.format(add_binary(a,b)))
