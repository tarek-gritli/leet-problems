# Runtime: 38ms, Beats 52.51% of users with Python3
# Memory: 16.48MB, Beats 94.55% of users with Python3

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s=set()
        l,r=0,1
        n=len(word)
        while r<n:
            while l<n and word[l].isalpha():
                l+=1
            r=l+1
            while r<n and word[r].isdigit():
                r+=1
            s.add(int(word[l:r])) if word[l:r] else None
            l=r+1
        if word.isdigit():
            return 1
        return len(s)