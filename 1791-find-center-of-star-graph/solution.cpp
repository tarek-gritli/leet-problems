// Runtime: 252 ms, Beats 16.35% of users with C++
// Memory: 96.05 MB, Beats 6.94% of users with C++

class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        map<int,int> node_count;
        for(auto edge: edges)
        {
            node_count[edge[0]]++;
            node_count[edge[1]]++;
        }
        for(auto node: node_count)
        {
            if(node.second==edges.size()) return node.first;
        }
        return -1;
    }
};