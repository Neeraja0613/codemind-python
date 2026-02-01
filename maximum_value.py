class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        c = []
        for i in strs:
            for j in i:
                if j.isalpha():
                    c.append(len(i))
                    break
            else:
                c.append(int(i))
        return max(c)        
