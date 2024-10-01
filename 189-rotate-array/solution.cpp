/*
    Performance:
    - Time: O(n).
    - Space: O(1) since it uses a constant amount of extra space.

    Runtime: 16ms, Beats 86.07% of users with C++
    Memory: 27.43MB, Beats 92.55% of users with C++
*/

class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        int n = nums.size();
        k = k % n;
        reverse(nums, 0, n - k - 1);
        reverse(nums, n - k, n - 1);
        reverse(nums, 0, n - 1);
    }

private:
    void reverse(vector<int> &nums, int start, int end)
    {
        while (start < end)
        {
            swap(nums[start], nums[end]);
            start++;
            end--;
        }
    }
};