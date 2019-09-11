# https://leetcode.com/problems/roman-to-integer/
# Passed: 64ms, 13.9MB

romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(s: str) -> int:
    r = 0
    for i in range(len(s)):
        try:
            if romans[s[i+1]] > romans[s[i]]:
                r -= romans[s[i]]
            else:
                r += romans[s[i]]
        except IndexError:
            r += romans[s[i]]
    return r

if __name__ == '__main__':
    # first test
    assert roman_to_int('III') == 3, 'First example'

    # second test
    assert roman_to_int('IV') == 4, 'Second example'

    # third test
    assert roman_to_int('IX') == 9, 'Third example'

    # fourth test
    assert roman_to_int('LVIII') == 58, 'Fourth example'

    # fifth test
    assert roman_to_int('MCMXCIV') == 1994, 'Fifth example'

