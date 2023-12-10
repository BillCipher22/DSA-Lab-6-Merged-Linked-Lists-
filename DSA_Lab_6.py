#Gary Delfin U. Berte
#BSCPE 2-6
#Data Structure and Algorithm

class Node_List:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def Merged_lists(list1, list2):
    Head = Node_List()
    Official = Head

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            Official.next = list1
            list1 = list1.next
        else:
            Official.next = list2
            list2 = list2.next

        Official = Official.next

    if list1 is not None:
        Official.next = list1
    elif list2 is not None:
        Official.next = list2

    return Head.next

def print_list(head):
    while head is not None:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

list_1 = Node_List(1, Node_List(3, Node_List(5, Node_List(7, Node_List(9)))))
list_2 = Node_List(2, Node_List(4, Node_List(6, Node_List(8, Node_List(10)))))

merged_list = Merged_lists(list_1, list_2)
print("Merged List:")
print_list(merged_list)
