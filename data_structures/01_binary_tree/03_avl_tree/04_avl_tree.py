# -*- coding: utf-8 -*-
"""

"""


def getRightMost(root):
    pass


def getLeftMost(root):
    pass


def my_max(a, b):
    pass


class my_node:
    pass


def getheight(node):
    pass


def leftrotation(node):
    pass


def rlrotation(node):
    pass


def lrrotation(node):
    pass


def rightrotation(node):
    pass


# del_node(self.root, data)
def del_node(root, data):
    if data == root.getdata():
        """
        left     | right
        ---------|---------
        not None | not None
        not None | None
        None     | not None
        None     | None
        """
        if root.getleft() is not None and root.getright() is not None:
            temp_data = getLeftMost(root.getright())
            root.setdata(temp_data)
            root.setright(del_node(root.getright(), temp_data))
        elif root.getleft() is not None:
            root = root.getleft()
        else:
            root = root.getright()

    elif data < root.getdata():
        if root.getleft() is None:
            print("No such data")
            return root
        else:
            root.setleft(del_node(root.getleft(), data))

    elif data > root.getdata():
        if root.getright() is None:
            return root
        else:
            root.setright(del_node(root.getright(), data))

    if root is None:
        return root

    r"""
     6           6           6      6
      \           \           \      \
       9  =>       9           9      9
     /  \           \         /      / \
     8  10           10      8       8 10

         6             6        6           6
        /             /        /           /
       3   =>        3        3           3
      / \           /          \         / \
     2   5         2            5       2   5
    """
    if getheight(root.getright()) - getheight(root.getleft()) == 2:
        if getheight(root.getright().getright()) > getheight(root.getright().getleft()):
            root = rightrotation(root)
        else:
            root = lrrotation(root)
    elif getheight(root.getright()) - getheight(root.getleft()) == -2:
        if getheight(root.getleft().getleft()) > getheight(root.getleft().getright()):
            root = leftrotation(root)
        else:
            root = rlrotation(root)

    height = my_max(getheight(root.getright()), getheight(root.getleft())) + 1
    root.setheight(height)
    return root



