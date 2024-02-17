class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    num1 = ''
    num2 = ''
    arr1 = []
    arr2 = []
    arr1.append(l1)
    arr2.append(l2)
    while arr1:
        node = arr1.pop()
        num1+=str(node.val)
        if node.next:
            arr1.append(node.next)
    while arr2:
        node = arr2.pop()
        num2+=str(node.val)
        if node.next:
            arr2.append(node.next)

    num1 = num1[::-1]
    num2 = num2[::-1]
    addition = str(int(num1) + int(num2))
    addition = addition[::-1]
    head = ListNode(int(addition[0]))
    current_node = head
    for i in range(1, len(addition)):
        new_node = ListNode(int(addition[i]))
        current_node.next = new_node
        current_node = new_node
    
    return head

print('*************************2.ADD TWO NUMBERS*************************')
print()
print('Enter List 1: ')
l1_list = list(map(int, input().split()))
print('Enter List 2: ')
l2_list = list(map(int, input().split()))
print()
print('Linked List 1:')

l1 = ListNode(l1_list[0])
current_node = l1
print(current_node.val, end='->')
for i in range(1, len(l1_list)):
    new_node = ListNode(l1_list[i])
    current_node.next = new_node
    current_node = new_node
    if i < len(l1_list)-1:
        print(current_node.val, end='->')
print(current_node.val)

print()
print('Linked List 2:')
l2 = ListNode(l2_list[0])
current_node = l2
print(current_node.val, end='->')
for i in range(1, len(l2_list)):
    new_node = ListNode(l2_list[i])
    current_node.next = new_node
    current_node = new_node
    if i < len(l2_list)-1:
        print(current_node.val, end='->')
print(current_node.val)

ans = addTwoNumbers(l1,l2)
array = []
array.append(ans)
        
print()
print('Addition of Two linked list is reverse order')
while array:
    current_node = array.pop()
    if current_node.next:
        print(current_node.val, end='->')
        array.append(current_node.next)
print(current_node.val)

