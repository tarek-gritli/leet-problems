// Runtime: 10ms, Beats 66.81% of users with Java
// Memory: 42.75MB, Beats 43.33% of users with Java

class Solution {
    public int characterReplacement(String s, int k) {
        int i=0;
        int n=s.length();
        int res=0;
        int maxf=0;
        int [] count=new int[26];
        for(int j=0;j<n;j++)
        {
            count[s.charAt(j)-'A']++;
            maxf=Math.max(maxf,count[s.charAt(j)-'A']);
            if(j-i+1-maxf>k)
            {
                count[s.charAt(i)-'A']--;
                i++;
            }
            res=Math.max(res,j-i+1);
        }
        return res;
    }
}