// Runtime: 4 ms, Beats 28.45% of users with C++
// Memory: 6.99 MB, Beats 14.24% of users with C++

class Solution {
public:
    int sum_chiff(int n)
    {
        int sum=0;
        while (n!=0)
        {
            sum+=pow(n%10,2);
            n=n/10;
        }
        return sum;
    }
    bool isHappy(int n) {
        set<int> s;
        while(n!=1 && s.find(n) == s.end())
        {
            s.insert(n);
            n=sum_chiff(n);
        }
        if(n==1) return true;
        else return false;
    }
};