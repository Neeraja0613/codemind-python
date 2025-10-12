class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x=sorted(score, reverse=True)
        r={}
        for i,s in enumerate(x):
            if i==0:
                r[s]="Gold Medal"
            elif i==1:
                r[s]="Silver Medal"
            elif i==2:
                r[s]="Bronze Medal"
            else:
                r[s]=str(i+1)
        return [r[s] for s in score]
