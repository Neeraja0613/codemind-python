class Solution:
    def intersection(self, a, b):
        # Your code here
        return sorted(set(set(a).intersection(b)))
