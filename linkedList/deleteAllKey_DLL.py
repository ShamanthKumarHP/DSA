# delete all occurences of key in DLL
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

class Solution():
    def deleteAllKey(self, head, key):
        temp = head
        while temp:
            if temp.data == key:
                if temp == head:
                    # just move head
                    head = temp.next
                else:
                    prevNode = temp.prev
                    nextNode = temp.next
                    prevNode.next = nextNode
                    if nextNode:
                        nextNode.prev = prevNode
            temp = temp.next
        return head


arr = [1,2,4,1,3]
object1 = DLLNode()
head = object1.convertArrDLL(arr)
object1.printDLL(head)

key = 1
solutionObj = Solution()
ans = solutionObj.deleteAllKey(head,key)
object1.printDLL(ans)