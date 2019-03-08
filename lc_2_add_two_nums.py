class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        sum_list = ListNode(None)
        first = sum_list
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num = val1 + val2 + carry
            carry = 1 if num >= 10 else 0
            sum_list.val = num % 10

            if (l1 and l1.next) or (l2 and l2.next) or carry == 1:
                sum_list.next = ListNode(None)
                sum_list = sum_list.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry == 1:
            sum_list.val = 1

        return first


l1_2 = ListNode(1)
l1_4 = ListNode(8)
# l1_3 = ListNode(9)
l1_2.next = l1_4
# l1_4.next = l1_3

l2_5 = ListNode(0)
# l2_6 = ListNode(9)
# l2_4 = ListNode(9)
# l2_5.next = l2_6
# l2_6.next = l2_4

def printList(node):
    if node is None: return
    print(node.val)
    printList(node.next)



# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

s = Solution()
printList(s.addTwoNumbers(l1_2, l2_5))