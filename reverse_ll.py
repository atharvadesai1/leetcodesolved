class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head:
        return head
    if not head.next:
        return head
    nums = []
    current_node = head
    while current_node:
        nums.append(current_node.val)
        current_node = current_node.next
    nums.reverse()

    top = ListNode()
    top.val = nums[0]
    top.next = ListNode()
    current_node = top.next
    for i in range(1,len(nums)):
        current_node.val = nums[i]
        if i != len(nums)-1:
            current_node.next = ListNode()
            current_node = current_node.next
    return top

print('*****************REVERSING THE LINKED LIST*****************')
print()
print('Enter the linked list: ')
l = list(map(int, input().split()))
print()
head = ListNode()
head.val = l[0]
head.next = ListNode()
current_node = head.next

for i in range(1,len(l)):
    current_node.val = l[i]
    if i != len(l)-1:
        current_node.next = ListNode()
        current_node = current_node.next

hnode = head
print('Linked List: ',end='')
while hnode.next:
    print(f'{hnode.val} => ',end='')
    hnode = hnode.next
print(f'{hnode.val}')

ans = reverseList(head)
cnode = ans
print('Reverse Linked List: ',end='')
while cnode.next:
    print(f'{cnode.val} => ',end='')
    cnode = cnode.next
print(f'{cnode.val}')