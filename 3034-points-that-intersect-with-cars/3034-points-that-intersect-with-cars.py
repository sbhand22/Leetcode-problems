class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        maxs,res=0,0
        for s,e in nums:
            if e>=maxs:
                res+=e-max(maxs,s)+1
            maxs=max(e+1,maxs) 
        return res

            
            
        