/* 
    Performance:
    - Time: O(log n) because it uses binary search to find the number.
    - Space: O(1) since it uses a constant amount of extra space.

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 7.56MB, Beats 70.52% of users with C++
*/

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int lo = 1;
        int hi = n;
        int mid,res;
        while (lo < hi) {
            mid = lo + (hi-lo) / 2;
            res = guess(mid);

            if(res == -1) hi = mid - 1;
            else if (res == 1) lo = mid + 1;
            else return mid;
        }
        return lo;
    }
};