// Runtime: 122ms, Beats 61.97% of users with C++
// Memory: 69.30MB, Beats 96.32% of users with C++

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        heapSort(nums);
        return nums;
    }
    
private:
    void heapSort(vector<int>& pq) {
        int n = pq.size();
        for(int i=n/2; i>=1;i--) {
            sink(pq, i, n);
        }

        while(n>1) {
            exch(pq,1,n--);
            sink(pq,1,n);
        }
    }
    bool less(const vector<int>& pq, int i, int j) {
        return pq[i-1] < pq[j-1];
    }
    void exch(vector<int>& pq, int i, int j) {
        int tmp = pq[i-1];
        pq[i-1] = pq[j-1];
        pq[j-1] = tmp;
    }
    void sink(vector<int>& pq, int k, int N) {
        while (2 * k <= N) {
            int j = 2 * k;
            if (j < N && less(pq, j, j + 1))
                j++;
            if(!less(pq,k,j)) break;
            exch(pq, j, k);
            k = j;
        }
    }
};