class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+=i + "endshaka"
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        temp=''
        # if s=='':
        #     return [""]
        for i in s:
            temp+=i
            if temp[-8:]=='endshaka':
                # if s[i]==' ':
                l.append(temp[:-8])
                temp=''
                # else:
                #     temp+=s[i]
                #     l.append(temp)
                #     temp=''
            # else:
                
        return l