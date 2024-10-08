/*
    Performance:
    - Time: O(n+m) where n and m denote the lengths of str1 and str2 respectively.
    - Space: O(n+m).

    Runtime: 3ms, Beats 58.64% of users with C++
    Memory: 8.75MB, Beats 30.54% of users with C++
*/

class Solution
{
public:
    string gcdOfStrings(string str1, string str2)
    {
        if (str1 + str2 != str2 + str1)
            return "";
        int size = gcd(str1.size(), str2.size());
        return str1.substr(0, size);
    }
};