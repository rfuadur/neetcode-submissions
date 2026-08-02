class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic.keys():
                dic[i]=1
            else: 
                dic[i]+=1
        sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)) 
        res=list(sorted_dict.keys())[:k]
        return res
            

        