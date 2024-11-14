/*
    Performance:
    - Time: O(log(n))
    - Space: O(1)

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 25.02MB, Beats 14.68% of users with C++
*/

class Solution
{
public:
    int singleNonDuplicate(vector<int> &nums)
    {
        int n = nums.size();
        int l = 0, r = n - 1;

        while (l < r)
        {
            int mid = l + (r - l) / 2;

            if ((mid - 1 < 0 || nums[mid - 1] != nums[mid]) && (mid + 1 == n || nums[mid] != nums[mid + 1]))
                return nums[mid];

            int subLeft;
            if (mid - 1 >= 0 && nums[mid - 1] != nums[mid])
            {
                subLeft = mid;
            }
            else
            {
                subLeft = mid - 1;
            }
            if (subLeft % 2 == 0)
            {
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
            }
        }

        return nums[l];
    }
};