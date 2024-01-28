// Runtime: 11ms, Beats 50.63% of users with C++
// Memory: 18.08MB, Beats 9.38% of users with C++

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res(2);
        int p=0,q=numbers.size()-1;
        while(p<q)
        {
            if(numbers[p]+numbers[q]>target) q--;
            if(numbers[p]+numbers[q]<target) p++;
            if(numbers[p]+numbers[q]==target) break;
        }
        res[0]=p+1;
        res[1]=q+1;
        return res;
    }
};