// Runtime: 35ms, Beats 100.00% of users with C++
// Memory: 16.47MB, Beats 7.34% of users with C++

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n>0 && (n & (n-1)) == 0;
    }
};