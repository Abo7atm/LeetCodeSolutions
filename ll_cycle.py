# https://leetcode.com/problems/linked-list-cycle
# Passed: 1112ms, 18.5MB

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    if head == None or head.next == None:
        return False
    
    current = head
    seen = []
    
    while current != None:
        if current.__hash__() in seen:
            return True
        else:
            seen.append(current.__hash__())
            current = current.next
    
    return False 
