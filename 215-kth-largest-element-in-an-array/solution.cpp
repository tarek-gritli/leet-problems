// Runtime: 66ms, Beats 96.66% of users with C++ 
// Memory: 64.80MB, Beats 11.54% of users with C++

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        ios::sync_with_stdio(0); cin.tie(0);
        priority_queue<int> pq;

        for(int num: nums) {
            pq.push(num);
        }
        while(k > 1) {
            pq.pop();
            k--;
        }
        return pq.top();
    }
};