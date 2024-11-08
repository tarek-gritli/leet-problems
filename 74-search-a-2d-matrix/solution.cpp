/*
    Performance:
    - Time: O(log(n*m))
    - Space: O(1)

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 12.20MB, Beats 77.53% of users with C++
*/
class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int m = matrix.size();
        int n = matrix[0].size();

        int lo = 0, hi = m - 1;

        while (lo <= hi)
        {
            int mid = (hi + lo) / 2;

            if (matrix[mid][n - 1] < target)
                lo = mid + 1;
            else if (matrix[mid][0] > target)
                hi = mid - 1;
            else
                break;
        }

        if (lo > hi)
            return false;

        int l = 0, r = n - 1;
        int row = (lo + hi) / 2;
        while (l <= r)
        {
            int m = (l + r) / 2;
            if (matrix[row][m] < target)
                l = m + 1;
            else if (matrix[row][m] > target)
                r = m - 1;
            else
                return true;
        }
        return false;
    }
};