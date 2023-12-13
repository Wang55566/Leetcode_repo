from typing import List

class Trie:
    def __init__(self):
        self.children = {}


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        root = Trie()
        strongPairs = []
        for x in nums:
            # root.chidren[x] = Trie()
            for y in nums:
                if abs(x - y) <= min(x,y):
                    strongPairs.append((x,y))

        m = 0
        for x, y in strongPairs:
            if x^y > m:
                m = x^y
        return m
