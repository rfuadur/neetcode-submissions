class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i!=j:
                    temp*=nums[j]
            l.append(temp)
        return l