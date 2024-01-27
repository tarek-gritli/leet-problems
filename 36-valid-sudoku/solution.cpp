// Runtime: 25ms, Beats 23.88% of users with C++
// Memory: 23.84MB, Beats 6.83% of users with C++

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //check if numbers on the same line are unique
        set<char> s;
        int i=0,j=0;
        while(i<9)
        {
            s.clear();
            j=0;
            while(j<9)
            {
                if(board[i][j]<='9' && board[i][j]>='1' && s.find(board[i][j])!=s.end()) return false;
                s.insert(board[i][j]);
                j++;
            }
            i++;
        }
        // check if numbers on same column are unique
        j=0;
        while(j<9)
        {
            s.clear();
            i=0;
            while(i<9)
            {
                if(board[i][j]<='9' && board[i][j]>='1' && s.find(board[i][j])!=s.end()) return false;
                s.insert(board[i][j]);
                i++;
            }
            j++;
        }
        // check if sub-boxes of the grid contain digits without repetition
        for(i=0;i<9;i+=3)
        {
            for(j=0;j<9;j+=3)
            {
                s.clear();
                for(int u=i;u<i+3;u++)
                {
                    for(int v=j;v<j+3;v++)
                    {
                        if(board[u][v]<='9' && board[u][v]>='1' && s.find(board[u][v])!=s.end()) return false;
                        s.insert(board[u][v]);
                    }
                }
            }
        }
        return true;
    }
};