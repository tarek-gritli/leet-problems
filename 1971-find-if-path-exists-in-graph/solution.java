// Runtime: 13ms, Beats 97.49% of users with Java
// Memory: 109.87MB, Beats 98.28% of users with Java

class QuickUnion {
    private int[] id;
    private int[] sz;

    public QuickUnion(int N) {
        id = new int[N];
        sz = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

    public int root(int i) {
        while (i != id[i])
            i = id[i];
        return i;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int rootp = root(p);
        int rootq = root(q);
        if (rootp == rootq)
            return;

        if (sz[rootp] < sz[rootq]) {
            id[rootp] = rootq;
            sz[rootq] += sz[rootp];
        } else {
            id[rootq] = rootp;
            sz[rootp] += sz[rootq];
        }
    }

}

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        QuickUnion uf = new QuickUnion(n);
        for (int[] edgs : edges) {
            uf.union(edgs[0], edgs[1]);
        }
        return uf.connected(source, destination);
    }
}