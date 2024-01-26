// Runtime: 93 ms, faster than 77.84% of C++ online submissions for Contains Duplicate.
// Memory: 75.12 MB, Beats 5.30% of users with C++

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> dup;
        for(auto el: nums) dup[el]++;
        for(auto el: dup)
        {
            if(el.second!=1) return true;
        }
        return false;
    }
};