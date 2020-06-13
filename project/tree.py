"""
Tree structure with basic methods built in
"""

from person import (Address, Person)


class Node:
    """
    A single entity in the tree
    """

    def __init__(self, person):
        pass

    def __str__(self):
        pass


class Tree:
    """
    A tree representation of the COVID-19 data
    """

    def __init__(self, csv_filename):
        pass

    # a method for taking a csv and producing a tree
        # call insert(id parent, id for each child)

    def insert(self, parent, child):
        """
        Inserts the node somewhere in the tree
        """
        pass

    def search(self, node):
        """
        Find the node in the tree. Return empty node
        if not found
        """
        pass

    def get_affected_percentage(self):
        """
        return the percentage of affected nodes in the 
        whole tree.
        """
        pass

    def print_all_nodes(self):
        """
        Print all nodes recusively
        """
        pass
