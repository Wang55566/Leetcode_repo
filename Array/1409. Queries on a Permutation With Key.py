from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        if not queries:
            return []

        p = []
        res = []

        for i in range(1, m + 1):
            p.append(i)

        for q in queries:
            index = p.index(q)
            res.append(index)
            num = p.pop(index)
            p.insert(0, num)
        return res
