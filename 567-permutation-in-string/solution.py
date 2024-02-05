# Runtime: 5000ms, Beats 5.01%of users with Python3
# Memory: 16.59MB, Beats 84.34% of users with Python3

class Solution:
    def isAnagram(self,s1,s2):
        if(len(s1)!=len(s2)):
            return False
        dicS1={}
        dicS2={}
        n=len(s1)
        for i in range (n):
            dicS1[s1[i]]=1+dicS1.get(s1[i],0)
            dicS2[s2[i]]=1+dicS2.get(s2[i],0)
        return dicS1 == dicS2
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        p=0
        n=len(s2)
        while(p<=n-window):
            if self.isAnagram(s2[p:p+window],s1):
                return True
            p+=1
        return False