# https://leetcode.com/problems/add-binary/
# Passed: 36ms, 3.7MB

def add_binary(a: str, b:str) -> str:
    return bin(int('0b'+a, 2)+int('0b'+b, 2))[2:]


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
