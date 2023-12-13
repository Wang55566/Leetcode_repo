class Solution:
    def countPoints(self, rings: str) -> int:
        hashMap = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }
        res = 0

        for i in range(0, len(rings), 2):

            hashMap[int(rings[i + 1])] += rings[i]

        for key in hashMap:
            if "R" in hashMap[key] and "G" in hashMap[key] and "B" in hashMap[key]:
                res += 1
        return res 
