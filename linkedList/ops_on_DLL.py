class DLLNode():
    def __init__(self, data = 0, back=None, next=None) -> None:
        self.data = data
        self.back = back
        self.next = next

    def convertArrDLL(self, arr):
        if not arr:
            return None
        head = DLLNode(arr[0])
        prev = head
        for i in range(1,len(arr)):
            temp = DLLNode(arr[i])
            temp.back = prev
            prev.next = temp
            prev = temp
        return head
    
    def printDLL(self, head):
        while head:
            print(head.data,end="->")
            head = head.next
        print()
        return

    def printReverseDLL(self, prev):
        while prev:
            print(prev.data, end="->")
            prev = prev.back
        print()
        return
    
    def deleteHead(self, head):
        if not head or head.next is None:
            return None
        prev = head
        head = head.next
        head.back = None
        prev.next = None
        return head
    
    def deleteTail(self, head):
        if not head or head.next is None:
            return None
        temp = head

        while head.next:
            head = head.next
        prev = head.back
        prev.next = None
        head.back = None
        return temp

    def deleteNode(self, head, k):
        if not head:
            return None
        temp = head
        cnt = 0
        while head:
            cnt = cnt + 1
            if cnt == k:
                break
            head = head.next
        
        if not head:
            print("not found")
            return temp
        
        prev = head.back
        front = head.next

        if not prev and not front:
            # only one element
            return None
        elif not prev:
            # first element
            head.next = None
            front.back = None
            return front
        elif not front:
            # last element
            prev.next = None
            head.back = None
            return temp
        else:
            prev.next = front
            front.back = prev
            head.back = None
            head.next = None
            return temp
        
    def insertBeforeNode(self,knode, new_val):
        prev = knode.back
        newNode = DLLNode(new_val, prev, knode)
        prev.next = newNode
        knode.back = newNode
        return head
    
    def reverseDLL(self, head):
        curr = head
        prev = None
        while curr:
            prev = curr.back
            curr.back = curr.next
            curr.next = prev
            curr = curr.back
        # prev will be point to last second node
        # prev's back will have address of last node
        return prev.back

arr = [1,2,4,1,3]
object1 = DLLNode()
head = object1.convertArrDLL(arr)
print(id(head))
print("original")
object1.printDLL(head)
print()

# head = object1.deleteHead(head)
# object1.printDLL(head)

# head = object1.deleteTail(head)
# object1.printDLL(head)

# head = object1.deleteNode(head,6)
# object1.printDLL(head)

# head = object1.insertBeforeNode(head.next.next.next, 3)
# object1.printDLL(head)

# head = object1.reverseDLL(head)
# object1.printDLL(head)

