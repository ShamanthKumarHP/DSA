# find pairs with given sum
# distinct elements will be there
# it is sorted 
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
    def pairsWithSumK(self, head, k):
        ans = []
        first = head
        
        while head.next:
            head = head.next
        last = head

        while first.data < last.data:
            if first.data + last.data == k:
                ans.append((first.data, last.data))
                first = first.next
                last = last.prev
            elif first.data + last.data > k:
                last = last.prev
            else:
                first = first.next
        return ans


arr = [1,2,3,4,5]
object1 = DLLNode()
head = object1.convertArrDLL(arr)
object1.printDLL(head)

key = 6
solutionObj = Solution()
ans = solutionObj.pairsWithSumK(head,key)
print(ans)