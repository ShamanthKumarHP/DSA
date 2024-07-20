# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def printLL(self, head):
        while head:
            print(head.val,end="->")
            head = head.next
        print()
        return

    def reverseLL(self, node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
    
    def getKthNode(self, node, k):
        temp = node
        cnt = 0
        while node:
            cnt = cnt + 1
            if cnt == k:
                return node
            node = node.next
        return None # num of elements is less than k 


    def reverseKGroup(self, head, k):
        curr = head
        prevLast = None
        while curr:
            kth_node = self.getKthNode(curr,k)
            if kth_node is None:
                prevLast.next = curr
                break
            else:
                next_node = kth_node.next # store
                kth_node.next = None # break the link
                reversed_LL = self.reverseLL(curr)
                print("reverse")
                self.printLL(reversed_LL)
                print()
                if prevLast is None:
                    head = reversed_LL               
                else:
                    prevLast.next = reversed_LL
                prevLast = curr
                curr = next_node
        return head

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3) 
a.next.next.next = ListNode(4)
obj = Solution()
head = obj.reverseKGroup(a, k=2)
print(obj.printLL(head))
