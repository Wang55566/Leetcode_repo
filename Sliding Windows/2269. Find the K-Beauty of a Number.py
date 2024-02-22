class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_in_strtype= str(num)
        counter = 0
        for i in range(len(num_in_strtype)-k+1):
            divisor = int(num_in_strtype[i:i+k])
            if divisor != 0:
                if num%divisor == 0:
                    counter +=1
        return counter
