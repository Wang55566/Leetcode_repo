class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        numList = []
        for i in range(n):
            numList.append(i + 1)

        i = 0
        while len(numList) > 1:
            i = (i + k - 1) % len(numList)
            numList.pop(i)
        return numList[0]
