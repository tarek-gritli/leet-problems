// Runtime: 96 ms, faster than 70.26% of C++ online submissions for Contains Duplicate.
// Memory: 73.22 MB, Beats 11.90% of users with C++

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n=nums.size();
        unordered_set<int> s;
        for(int el: nums)
        {
            if(s.find(el)!=s.end()) return true;
            s.insert(el);
        }
        return false;

    }
};