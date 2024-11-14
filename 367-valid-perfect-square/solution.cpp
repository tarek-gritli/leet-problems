/*
    Performance:
    - Time: O(log(n))
    - Space: O(1)

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 7.34MB, Beats 50.68% of users with C++
*/

class Solution
{
public:
    bool isPerfectSquare(int num)
    {
        if (num == 1)
            return true;

        int l = 1, r = num / 2;
        while (l <= r)
        {
            long mid = (l + r) / 2;

            if (mid * mid > num)
                r = mid - 1;
            else if (mid * mid < num)
                l = mid + 1;
            else
                return true;
        }
        return false;
    }
};