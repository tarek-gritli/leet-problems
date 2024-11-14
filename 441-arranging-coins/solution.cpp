/*
    Performance:
    - Time: O(log(n))
    - Space: O(1)

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 8.51MB, Beats 67.75% of users with C++
*/

class Solution
{
public:
    int arrangeCoins(int n)
    {
        long left = 1, right = n, ans;

        while (left <= right)
        {
            long mid = (left + right) / 2;
            long coins = mid * (mid + 1) / 2;

            if (coins > n)
                right = mid - 1;
            else if (coins < n)
            {
                left = mid + 1;
                ans = mid;
            }
            else
                return mid;
        }
        return ans;
    }
};