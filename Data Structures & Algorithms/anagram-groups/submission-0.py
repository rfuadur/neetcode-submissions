class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        seen=[]
        for i in range(len(strs)):
            if strs[i] not in seen:
                t=[strs[i]]
            # seen=[strs[i]]
            else:
                continue

            for j in range(i+1,len(strs)):
                if sorted(strs[i])==sorted(strs[j]) and strs[j] not in seen:
                    t.append(strs[j])
                    # seen.append(strs[j])

                else:
                    continue
            out.append(t)
            for x in t:
                seen.append(x)
# print(type(out))
        out.sort(key=len)
        return out