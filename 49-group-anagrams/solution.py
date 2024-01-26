# Runtime: 92ms, Beats 65.13% of users with Python3
# Memory: 22.07MB, Beats 28.58% of users with Python3

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams={}
        for el in strs:
            count=[0]*26
            for c in el:
                count[ord(c)-ord('a')]+=1
            count=tuple(count) #because in python list cannot be a key
            if count in anagrams.keys():
                anagrams[count].append(el)
            else:
                anagrams[count]=[el]
        return anagrams.values()
