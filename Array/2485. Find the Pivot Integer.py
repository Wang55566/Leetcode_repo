class Solution:
    def pivotInteger(self, n: int) -> int:
        list_n=[]
        for i in range(1,n+1):
            list_n.append(i)

        for i in range(list_n):

            if sum(list_n[:i+1]) == sum(list_n[i:]):
                return list_n[i]
