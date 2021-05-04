#!/usr/bin/python3
"""Private class Node and public class linkedlist"""


class Node:
    """Node defines the data type"""
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter"""
        if type(value) is not type(self) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """python linked list"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """inserts node at sorted position"""
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return self.head
        if value <= self.head.data:
            temp.next_node = self.head
            self.head = temp
            return
        trav = self.head
        while trav.next_node is not None:
            if value < trav.next_node.data:
                break
            trav = trav.next_node
        if trav.next_node is None and value > trav.data:
            trav.next_node = temp
        else:
            temp.next_node = trav.next_node
            trav.next_node = temp
        return self.head

    def __str__(self):
        """printable func for print()"""
        temp = self.head
        st = ""
        while temp is not None:
            st = st + str(temp.data) + "\n"
            temp = temp.next_node
        nst = st[:len(st) - 1]
        return nst
