class Solution:
    def segregateElements(self, arr):
        pos = []
        neg = []
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        
        # Overwrite arr in-place
        for i in range(len(pos)):
            arr[i] = pos[i]
        for i in range(len(neg)):
            arr[i + len(pos)] = neg[i]
