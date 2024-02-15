// Runtime: 0ms, Beats 100.00% of users with C++ 
// Memory: 7.02MB, Beats 35.70% of users with C++


class Solution {
public:
    int hammingWeight(uint32_t n) {
        return __builtin_popcount(n);
    }
};