// Runtime: 4ms, Beats 46.70% of users with C++
// Memory: 7.07MB, Beats 61.35% of users with C++

class Solution {
public:
    bool judgeSquareSum(int c) {
        for(long long a = 0; a*a <= c; a++) {
            double b = sqrt(c-a*a);
            if (b== (int) b) return true;
        }
        return false;
    }
};