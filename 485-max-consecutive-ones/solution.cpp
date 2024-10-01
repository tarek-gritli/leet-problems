/*
    Performance:
    - Time: O(n).
    - Space: O(1) since it uses a constant amount of extra space.

    Runtime: 31ms, Beats 50.95% of users with C++
    Memory: 49.14MB, Beats 14.27% of users with C++
*/

class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {
        int max_cnt = 0;
        int cnt = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            if (nums[i] == 0)
            {
                max_cnt = max(cnt, max_cnt);
                cnt = 0;
            }
            else
            {
                cnt++;
            }
        }
        return max(cnt, max_cnt);
    }
};