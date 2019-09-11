# https://leetcode.com/problems/linked-list-cycle

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    """
    sudo code
    ---------
    this is what a problem should look like
    """
    current = head
    while current.next != None:

