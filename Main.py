from typing import Optional


class Node:
    """
    Provide necessary documentation
    """
    def __init__(self, data=None, next=None):
        """
        Provide necessary documentation
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    Provide necessary documentation
    """
    def __init__(self):
        """
        Initialize the head
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Insert node at end of the list
        :param data: integer data that will be used to create a node
        """


    def status(self):
        """
        It prints all the elements of list.
        """
      


class Solution:
    """
    Provide necessary documentation
    """
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[LinkedList]:
        """
        :param first_list: Linkedlist with non-negative integers
        :param second_list: Linkedlist with non-negative integers
        :return: returns the sum as a linked list
        """
        
        
        

first_list = LinkedList()

second_list = LinkedList()

data_for_first_list = list(map(int, input().strip().split(" ")))

for data in data_for_first_list:
    first_list.insert_at_end(data)

data_for_second_list = list(map(int, input().strip().split(" ")))

for data in data_for_second_list:
    second_list.insert_at_end(data)

solution = Solution()

new_list = solution.addTwoNumbers(first_list, second_list)

new_list.status()
