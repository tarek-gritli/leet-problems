// Runtime: 0ms, Beats 100.00% of users with C++
// Memory: 9.40MB, Beats 92.95% of users with C++

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer(n);
        for (int i=1;i<=n;i++) {
            if(i%3==0) {
                answer[i-1] = (i%5) ? "Fizz" : "FizzBuzz";
            } else{
                answer[i-1] = (i%5) ? to_string(i) : "Buzz";
            }
        }
        return answer;
    }
};

