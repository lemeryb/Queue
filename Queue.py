from LinkedList import LinkedList

# Title: Linked List Queues & Stacks
# Date: 3/9/20
# Author: Benjamin Lemery
# This program demonstrates how to create and manipulate a queue


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def push(self,data):
        self.list.add_to_end(data)

    def pop(self):
        return self.list.remove_from_head()


