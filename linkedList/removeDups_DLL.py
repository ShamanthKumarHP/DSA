# remove duplicates from sorted LL
class DLLNode():
    def __init__(self, data = 0, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
    
    def printDLL(self, head):
        while head:
            print(head.data,end="->")
            head = head.next
        print()
        return

    def findTail(self, head):
        while head.next:
            head = head.next
        return head

    def convertArrDLL(self, arr):
        if not arr:
            return None
        head = DLLNode(arr[0])
        prev = head
        for i in range(1,len(arr)):
            temp = DLLNode(arr[i])
            temp.prev = prev
            prev.next = temp
            prev = temp
        return head
    
    def printReverseDLL(self, prev):
        while prev:
            print(prev.data, end="->")
            prev = prev.prev
        print()
        return

class Solution():
    def removeDups(self, head):
        curr = head
        while curr:
            temp = curr
            while temp and curr.data == temp.data:
                temp = temp.next
            curr.next = temp
            if temp:
                temp.prev = curr
            curr = curr.next
        return head


arr = [1,1,1,2,2,3,4,5,5]
object1 = DLLNode()
head = object1.convertArrDLL(arr)
object1.printDLL(head)


solutionObj = Solution()
ans = solutionObj.removeDups(head)
object1.printDLL(ans)

object1.printReverseDLL(object1.findTail(ans))