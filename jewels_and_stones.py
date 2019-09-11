# https://leetcode.com/problems/jewels-and-stones/
# Passed: 28ms, 13.9MB

def numJewelsInStones(J: str, S: str) -> int:

    return sum([S.count(j) for j in list(J)])
    J = list(J)
    S = list(S)

    res = []
    for j in J:
        res.append(S.count(j)) 
    return sum(res)

if __name__=='__main__':
    print(numJewelsInStones('z', 'Z'))
