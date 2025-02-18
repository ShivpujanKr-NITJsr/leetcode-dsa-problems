class Solution {
    public int maxDepth(String s) {

        int open =0;
        int ans=0;

        int i=0;
        int l=s.length();

        while(i<l){

            char c= s.charAt(i);

            if(c=='('){
                open+=1;
            }else if(c==')'){
                ans=Math.max(ans,open);
                open-=1;
            }
            i+=1;
        }
        return ans;
        
    }
}