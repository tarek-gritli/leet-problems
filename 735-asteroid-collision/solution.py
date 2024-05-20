# Runtime: 74ms, Beats 92.16% of users with Python3
# Memory: 17.71MB, Beats 90.23% of users with Python3

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for num in asteroids:
            while st and num < 0 and st[-1]>0:
                if -num > st[-1]:
                    st.pop()
                    continue
                elif -num == st[-1]:
                    st.pop()
                break
            else:
                st.append(num)
        return st