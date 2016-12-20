# First try:

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printNode(self):
        currentNode = self
        while not currentNode == None:
            print currentNode.val
            currentNode = currentNode.next
            
def removeNthFromEnd(head, n):
    length = 0
    currentNode = head
    while not currentNode == None:
        length = length + 1
        currentNode = currentNode.next
    currentNode = head
    previousNode = head
    index = length - n + 1
    currentIndex = 1
    while not currentIndex == index and not currentNode == None:
        previousNode = currentNode
        currentNode = currentNode.next
        currentIndex = currentIndex + 1
    if not currentNode == None:
        previousNode.next = currentNode.next
        
        