# Definition for singly-linked list.
# one solution - TC = 0(3N), SC = 0(1)
# second solution -  TC = O(1), SC = auxilary space(recursion)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # approach one
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    
    def add1(self, head):
        temp = head
        carry = 1
        while temp:
            temp.val = temp.val + carry
            if temp.val < 10:
                carry = 0
                break
            else:
                temp.val = 0
                temp = temp.next
        return carry

    def solutionOne(self, head):
        # reverse 
        # add 1
        # reverse
        rev1 = self.reverse(head)
        carry1 = self.add1(rev1)
        if carry1:
            node = ListNode(val = 1)
            rev2 = self.reverse(rev1)
            node.next = rev2
            return node
        else:
            return self.reverse(rev1)
    
    def printLL(self, head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()

    def recursion(self, node):
        if node is None:
            return 1 #carry => adding 1
        carry = self.recursion(node.next)
        node.val = node.val + carry
        if node.val < 10:
            return 0
        else:
            node.val = 0
            return 1

    def solutionTwo(self, head):
        carry = self.recursion(head)
        if carry:
            node = ListNode(1)
            node.next = head
            return node
        else:
            return head
    
a = ListNode(1)
a.next = ListNode(9)

obj = Solution()
# obj.printLL(a)
# head = obj.solutionOne(a)
# obj.printLL(head)

head = (obj.solutionTwo(a))
obj.printLL(head)

  