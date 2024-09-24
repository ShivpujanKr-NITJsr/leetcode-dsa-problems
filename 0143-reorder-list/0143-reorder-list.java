/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        Stack<Integer> st=new Stack<>();

        ListNode f=head;

        ListNode s=head;
        if(head==null) return ;

        while(s.next!=null && s.next.next!=null){
            f=f.next;
            s=s.next.next;
        }

        ListNode m=f.next;
        f.next=null;

        ListNode h=head;

        ListNode cu=m;
        ListNode pre=null;

        // System.out.println(m.val+" "+f.val);
        while(cu!=null){
            ListNode tk=cu.next;
            cu.next=pre;
            pre=cu;
            cu=tk;

        }

        m=pre;
        while(h!=null){
            ListNode cur=h.next;
            h.next=m;
            if(m!=null)
            m=m.next;
            
            if(h.next!=null)
            h.next.next=cur;
            h=cur;
        }
    }
}