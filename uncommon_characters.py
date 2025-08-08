#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        s1=set(s1)
        s2=set(s2)
        r=[]
        for i in s1:
            if i not in s2:
                r.append(i)
        for i in s2:
            if i not in s1:
                r.append(i)
        return ''.join(sorted(r))
