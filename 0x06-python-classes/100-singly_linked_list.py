#!/usr/bin/python3

"""node class of linked list"""


class Node:
    """
    """
    def __init__(self, data, next_node=None):
        """
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        """
        if not isinstance(value, int):
            raise TypeError("100-singly_linked_list.py")
        self.__data = value

    @property
    def next_node(self):
        """
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        """
        if value == None:
            pass
        elif not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

        
"""SinglyLinkedList class"""



class SinglyLinkedList:
    """
    """
    def __init__(self):
        """
        """
        self.__head = None

    @property
    def add_node(self, value=0):
        new_node = Node(value)
        if value <= self.__head.data:
            new_node.next_node(self.__head, None)
            self.__head.next_node(None)
        else:
            new_node.next_node(None)
            self.__head.next_node(new_node)
    
    def sorted_insert(self, value):
        if self.__head == None:
            self.__head = Node(value, None)
        elif self.__head.next_node == None:
                self.add_node(value)
        return self.__head
