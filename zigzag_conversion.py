# https://leetcode.com/problems/zigzag-conversion/ 
# Passed: 84ms, 14MB

def convert(s, n_rows):
    # anomalies
    if n_rows == 0 or s == '':
        return ''
    elif n_rows > len(s):
        return s

    # init empty dict to store 'levels'
    d = dict.fromkeys([i for i in range(1, n_rows+1)])

    # counter to facilitate counting 1->2->3->2->1...
    counter = 1

    # to reverse counting after reaching limit (numRows)
    adder = 1

    for i in range(len(s)):

        if not d[counter]:
            d[counter] = []

        d[counter].append(s[i])
        
        # counting levels
        if n_rows > 1:
            counter += adder
            if counter == n_rows or counter == 1:
                adder *= -1 

    result = [char for lvl in list(d.keys()) for char in d[lvl]]
    return(''.join(result))

if __name__=='__main__':
    print(convert('PAYPALISHIRING', 4))
    print(convert('PAYPALISHIRING', 3))

