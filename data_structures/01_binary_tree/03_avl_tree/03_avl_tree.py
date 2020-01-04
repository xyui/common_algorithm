# -*- coding: utf-8 -*-
"""

"""


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


# insert_node(self.root, data)
def insert_node(node, data):
    if node is None:
        return my_node(data)

    if data < node.getdata():
        node.setleft(insert_node(node.getleft(), data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2:  # an unbalance detected
            if data < node.getleft().getdata():  # new node is the left child of the left child
                node = leftrotation(node)
            else:
                node = rlrotation(node)  # new node is the right child of the left child
    else:
        node.setright(insert_node(node.getright(), data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)

    h1 = my_max(getheight(node.getright()), getheight(node.getleft())) + 1
    node.setheight(h1)
    return node
