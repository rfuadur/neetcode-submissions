class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        
        r=0
        c=1
        nums=list(set(nums))
        nums=sorted(nums)
        for i in range(len(nums)):
            if i!=0:
                if nums[i]==nums[i-1]+1:
                    c+=1
                else:
                    if c>r:
                        r=c
                        c=1
                    else:
                        c=1       
        if c>r:
            r=c
        return r
