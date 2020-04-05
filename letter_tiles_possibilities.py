# https://leetcode.com/problems/letter-tile-possibilities/

from itertools import permutations as pt, chain

def numTilePossibilites(tiles):
    l = list(tiles)
    p = chain.from_iterable(pt(l, i) for i in range(len(l) + 1))
    r = set(p)
    return len(r) - 1
