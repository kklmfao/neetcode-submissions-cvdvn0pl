# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        l1_curr = l1
        l2_curr = l2
        carry = 0

        result = ListNode()
        result_curr = result
        last_node = None

        while l1_curr is not None or l2_curr is not None:
            temp = result_curr

            if l1_curr is not None and l2_curr is not None: # Handle l1_curr and l2_curr both is not None
                x = l1_curr.val + l2_curr.val + carry
                
                if x >= 10:
                    carry = 1
                    digit = x % 10
                else:
                    carry = 0
                    digit = x


                result_curr.val = digit
                result_curr.next = ListNode()
                result_curr = result_curr.next

                l1_curr = l1_curr.next
                l2_curr = l2_curr.next    
            elif l1_curr is not None and l2_curr is None: # Handle l1_curr is not None and l2_curr is None
                x = l1_curr.val + carry

                if x >= 10:
                    carry = 1
                    digit = x % 10
                else:
                    carry = 0
                    digit = x

                result_curr.val = digit
                result_curr.next = ListNode()
                result_curr = result_curr.next

                l1_curr = l1_curr.next
            elif l1_curr is None and l2_curr is not None: # Handle l1_curr is None and l2_curr is not None
                x = l2_curr.val + carry

                if x >= 10:
                    carry = 1
                    digit = x % 10
                else:
                    carry = 0
                    digit = x

                result_curr.val = digit
                result_curr.next = ListNode()
                result_curr = result_curr.next            

                l2_curr = l2_curr.next

            if l1_curr is None and l2_curr is None:
                last_node = temp

        if carry == 1:
            result_curr.val = 1
            result_curr.next = None
        else:
            last_node.next = None

        return result
                



                

