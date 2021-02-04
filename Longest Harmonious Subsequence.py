class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=collections.defaultdict(lambda:0)
        for i in range(0,len(nums)):
            d[nums[i]]+=1
        maxi=0
        for i in d.keys():
            if(d.get(i+1,"E")!="E"):
                maxi=max(maxi,d[i]+d[i+1])
        return maxi        
        
