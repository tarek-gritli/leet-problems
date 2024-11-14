/*
    Performance:
    - Time: O(log(n))
    - Space: O(1)

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 8.38MB, Beats 18.73% of users with C++
*/

#define ll long long
class Solution
{
public:
    int mySqrt(int x)
    {
        if (x == 0 || x == 1)
            return x;
        ll l = 1, r = x / 2, mid;

        while (l <= r)
        {
            mid = (l + r) / 2;

            if (mid * mid > x)
                r = mid - 1;
            else if (mid * mid < x)
                l = mid + 1;
            else
                return mid;
        }
        if (mid * mid > x)
            return mid - 1;
        else
            return mid;
    }
};