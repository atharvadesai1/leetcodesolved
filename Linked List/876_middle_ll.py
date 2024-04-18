class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(self, head):
    if not head:
        return head
    length_ll = 0
    current_node = head

    while current_node:
        length_ll += 1
        current_node = current_node.next

    print(length_ll)
    if length_ll%2 == 1:
        mid = (length_ll + 1)/2
    else:
        mid = (length_ll + 2)/2
    
    counter = 1
    current_node = head
    while counter <= mid:
        if counter == mid:
            pointer = current_node
            return pointer
        counter += 1
        current_node = current_node.next