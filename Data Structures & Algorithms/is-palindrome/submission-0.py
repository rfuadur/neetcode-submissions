class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i!=' ' and i.isalnum():
                a+=i
        a=a.upper()
        for i in range(len(a)//2):
            if a[i]==a[-(i+1)]:
                continue
            else:
                return False
        return True 