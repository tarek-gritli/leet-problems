/*
    Performance:
    - Time: O(n*log(max(piles)))
    - Space: O(1)

    Runtime: 10ms, Beats 52.11% of users with C++
    Memory: 21.71MB, Beats 43.91% of users with C++
*/
#define all(a) a.begin(), a.end()
#define ll long long
class Solution
{
public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        auto p = minmax_element(all(piles));
        int l = 1, r = *p.second;
        int res = r;
        while (l <= r)
        {
            int bph = l + (r - l) / 2;

            ll hoursNeeded = compute_hours(bph, piles);
            if (hoursNeeded <= h)
            {
                r = bph - 1;
                res = bph;
            }
            else
                l = bph + 1;
        }
        return res;
    }

private:
    ll compute_hours(int bph, vector<int> &piles)
    {
        ll hoursNeeded = 0;
        for (int i = 0; i < piles.size(); i++)
        {
            if (piles[i] <= bph)
                hoursNeeded++;
            else
            {
                hoursNeeded += (piles[i] / bph);
                if (piles[i] % bph)
                    hoursNeeded++;
            }
        }
        return hoursNeeded;
    }
};