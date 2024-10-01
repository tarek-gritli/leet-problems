/*
    Performance:
    - Time: O(n).
    - Space: O(n).

    Runtime: 46ms, Beats 99.35% of users with C++
    Memory: 45.43MB, Beats 45.99% of users with C++
*/

class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int n = nums.size();
        unordered_map<int, int> mp;
        int sum = 0, cnt = 0;
        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            if (sum == k)
            {
                cnt++;
            }
            if (mp.find(sum - k) != mp.end())
            {
                cnt += mp[sum - k];
            }
            mp[sum]++;
        }

        return cnt;
    }
};