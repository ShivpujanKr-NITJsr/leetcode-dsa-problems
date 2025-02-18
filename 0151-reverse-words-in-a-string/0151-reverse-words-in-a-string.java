class Solution {
    public String reverseWords(String s) {
        s=s.trim();

        StringBuilder ans=new StringBuilder();

        String temp="";

        for(int i=s.length()-1;i>=0;i--){

            if(s.charAt(i)!=' '){
                temp=s.charAt(i)+temp;
            }else{
                ans.append(temp+" ");
                temp="";
                while(i>0 && s.charAt(i-1)==' '){
                    i-=1;
                }
            }
        }
        ans.append(temp);
        return ans.toString();
        
    }
}