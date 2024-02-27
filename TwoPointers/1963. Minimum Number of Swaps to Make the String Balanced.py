class Solution:
    def minSwaps(self, s: str) -> int:
        listedS = list(s)
        opening_counter = 0
        closing_counter = 0
        i = 0
        p2_idx = len(listedS)-1
        swap_counter = 0
        while i < p2_idx:
            if listedS[i] == "]":
                closing_counter+= 1
            else:
                opening_counter+= 1

            if closing_counter > opening_counter:
                while listedS[p2_idx] == "]":
                    p2_idx-= 1
                # listedS[i],listedS[p2_idx] = listedS[p2_idx],listedS[i]
                # print(listedS)
                p2_idx-= 1
                swap_counter+= 1
                opening_counter += 1
                closing_counter -= 1
            i += 1
        return swap_counter
