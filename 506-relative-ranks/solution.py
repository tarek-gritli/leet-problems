# Runtime: 61ms, Beats 75.66% of users with Python3
# Memory: 17.59MB, Beats 89.05% of users with Python 3

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores= sorted(score,reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ranks ={score: medals[i] if i<3 else str(i+1) for i,score in enumerate(sorted_scores)}
        return [ranks[score] for score in score]

        