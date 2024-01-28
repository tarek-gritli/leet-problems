// Runtime: 4ms, Beats 93.68% of users with C++
// Memory: 18.06MB, Beats 9.38% of users with C++

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res(2);
        int p=0,comp=target-numbers[p],n=numbers.size();
        while(!binary_search(numbers.begin()+p+1,numbers.end(),comp))
        {
            p++;
            comp=target-numbers[p];
        }
        res[0]=p+1;
        for(int i=p+1;i<n;i++)
        {
            if(numbers[i]==comp)
            {
                res[1]=i+1;
                break;
            }
        }
        return res;
    }
};