# https://takeuforward.org/data-structure/flattening-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child
class Solution:
    # approach one
    # go to all elements, collect it in new arrayy, sort it, construct new LL
    # TC: O(M*N) + (M*N)log(M*N) + (M*N)
    # SC: 0(M*N) + O(M*N)


    # better
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        res = dummy
        while l1 and l2:
            if l1.val < l2.val:
                res.child = l1
                res = res.child
                l1 = l1.child
            else:
                res.child = l2
                res = res.child
                l2 = l2.child
            # point 'next' pointer to null. good to have
            res.next = None
        
        if l1:
            res.child = l1
        elif l2:
            res.child = l2
        
        # good to have
        if dummy.child: 
            dummy.child.next = None

        return dummy.child
    
    def mergeRecursion(self, head):
        if not head or not head.next:
            return head
        mergedHead = self.mergeRecursion(head.next)
        new_head = self.merge(head, mergedHead)
        return new_head
    
    def iterative(self, head):
        if not head or head.next is None:
            return head

        prev = None
        curr = head
        while curr:
            temp = curr.next
            prev = self.merge(prev, curr)
            curr = temp
        return prev

    def flatten_ll(self, head):
        # as children in each parent node are already in sorted
        # we can leverage merge sort of two LL
        
        # method 1 recursion
        # return self.mergeRecursion(head)

        # method 2 without recursion
        return self.iterative(head)
    
    def printOriginalLinkedList(self, head, depth):
        while head:
            print(head.val, end="")

            # If child exists, recursively
            # print it with indentation
            if head.child:
                print(" -> ", end="")
                self.printOriginalLinkedList(head.child, depth + 1)

            # Add vertical bars
            # for each level in the grid
            if head.next:
                print()
                print("| " * depth, end="")
            head = head.next
    
    def printLinkedList(self, head):
        while head:
            print(head.val, end=" ")
            head = head.child
        print()

head = ListNode(5)
head.child = ListNode(14)
head.next = ListNode(10)
head.next.child = ListNode(24)
head.next.next = ListNode(12)
head.next.next.child = ListNode(20)
head.next.next.child.child = ListNode(30)
head.next.next.next = ListNode(7)
head.next.next.next.child = ListNode(17)

obj = Solution()
print("Original linked list:")
obj.printOriginalLinkedList(head, 0)

flattened = obj.flatten_ll(head)
print("\nFlattened linked list: ", end="")
obj.printLinkedList(flattened)
