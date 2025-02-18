class Solution {
    public String removeOuterParentheses(String s) {

        int open=0; int close=0;
        StringBuilder ans = new StringBuilder("");

        int i=0;
        int l=s.length();
        int index=-1;

        while(i<l){
            if(s.charAt(i)=='('){
                if(open==0){
                    index=i;
                }
                open+=1;
            }else{
                close+=1;
                if(close==open){
                    String temp=s.substring(index+1,index+close+open-1);
ans.append(temp);
close=0;open=0;
                }
            }
            i+=1;
        }

        return ans.toString();
        
    }
}