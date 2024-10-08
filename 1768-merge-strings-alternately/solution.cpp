/*
    Performance:
    - Time: O(n1+n2) where n1 and n2 denote the lengths of word1 and word2 respectively.
    - Space: O(1).

    Runtime: 0ms, Beats 100.00% of users with C++
    Memory: 7.96MB, Beats 36.26% of users with C++
*/
#include <bits/stdc++.h>
class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        int n1 = word1.size();
        int n2 = word2.size();
        int i = 0, j = 0;
        string res = "";
        while (i < n1 && j < n2)
        {
            if (i <= j)
            {
                res += word1[i];
                i++;
            }
            else
            {
                res += word2[j];
                j++;
            }
        }
        while (i < n1)
        {
            res += word1[i];
            i++;
        }
        while (j < n2)
        {
            res += word2[j];
            j++;
        }
        return res;
    }
};