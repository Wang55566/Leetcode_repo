class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        p1 = 0
        p2 = 0

        T = 0
        F = 0
        ans = 0
        while p2 < len(answerKey):
            if answerKey[p2] == "T":
                T+=1
            else:
                F+=1

            if T <= k or F <= k:
                p2+=1
            else:
                p1 +=1
                p2 +=1
                if answerKey[p1-1] == "T":
                    T-=1
                else:
                    F-=1

        ans = p2 -p1



        if T == 0 or F == 0:
            return len(answerKey)

        return ans
