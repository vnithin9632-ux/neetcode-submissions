class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): 
            matching_1 = {}
            for i, j in enumerate(s):
                if j in matching_1: 
                    matching_1[j] +=1
                else:
                    matching_1[j] = 1
            matching_2 = {}
            for i, j in enumerate(t):
                if j in matching_2: 
                    matching_2[j] +=1
                else:
                    matching_2[j] = 1
            if matching_1 == matching_2:
                return True
            else: 
                return False
        else: 
            return False