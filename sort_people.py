class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x=zip(heights,names)
        n=sorted(x,reverse=True)
        return [i for _,i in n]
