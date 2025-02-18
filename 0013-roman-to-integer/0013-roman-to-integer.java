class Solution {
    public int romanToInt(String s) {

        int l=s.length();

        HashMap<Character,Integer> hm=new HashMap<>();

        hm.put('I',1);hm.put('V',5);hm.put('X',10);hm.put('L',50);
        hm.put('C',100);hm.put('D',500);hm.put('M',1000);
int ans=hm.get(s.charAt(l-1));
// System.out.println(ans+"-");
        for(int i=l-2;i>=0;i--){
            char c=s.charAt(i);
            char c2=s.charAt(i+1);

            int cvalue=hm.get(c);
            int cvalue2=hm.get(c2);

            if(cvalue>=cvalue2){
                ans+=cvalue;
            }else{
                ans-=cvalue;
            }
            // System.out.println(ans+"-"+cvalue);

        }
        return ans;
        
    }
}