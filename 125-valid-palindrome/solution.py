# Runtime: 33ms, Beats 98.51% of users with Python3
# Memory: 17.79MB, Beats 60.73% of users with Python3



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=re.findall("[a-zA-Z0-9]",s)
        p=0
        q=len(l)-1
        while(p<q):
            if(l[p].lower()!=l[q].lower()):
                return False
            p+=1
            q-=1
        return p>=q
        