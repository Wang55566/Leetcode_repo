from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        def helperFunction(str1, str2):
            obj1_odd = {}
            obj1_even = {}

            obj2_odd = {}
            obj2_even = {}

            # str1
            for i in range(len(str1)):
                if i % 2 == 0:
                    if str1[i] not in obj1_even:
                        obj1_even[str1[i]] = 1
                    else:
                        obj1_even[str1[i]] += 1
                elif i % 2 != 0:
                    if str1[i] not in obj1_odd:
                        obj1_odd[str1[i]] = 1
                    else:
                        obj1_odd[str1[i]] += 1
            # str2
            for i in range(len(str2)):
                if i % 2 == 0:
                    if str2[i] not in obj2_even:
                        obj2_even[str2[i]] = 1
                    else:
                        obj2_even[str2[i]] += 1
                elif i % 2 != 0:
                    if str2[i] not in obj2_odd:
                        obj2_odd[str2[i]] = 1
                    else:
                        obj2_odd[str2[i]] += 1

            # compare even
            key1_even = obj1_even.keys()
            key2_even = obj2_even.keys()
            for k in key1_even:
                if k not in key2_even:
                    return False
                if obj1_even[k] != obj2_even[k]:
                    return False

            # compare odd
            key1_odd = obj1_odd.keys()
            key2_odd = obj2_odd.keys()

            for k in key1_odd:
                if k not in key2_odd:
                    return False
                if obj1_odd[k] != obj2_odd[k]:
                    return False

            return True


        stack = []

        for string in words:
            if not stack:
                stack.append(string)
            else:
                x= False
                for stack_str in stack:
                    if helperFunction(stack_str, string):
                        x= True
                if not x:
                    stack.append(string)


        return len(stack)
