# Runtime: 505ms, Beats 69.20% of users with Python3
# Memory: 18.05MB, Beats 88.79% of users with Python3

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        for i in range(len(arr)-1,-1,-1):
            tmp = arr[i]
            arr[i] = maxi
            maxi = max(maxi,tmp)
        return arr

