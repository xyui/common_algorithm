#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class RedBlackTree:
    def __init__(self, label=None, color=0, parent=None, left=None, right=None):
        """Initialize a new Red-Black Tree node with the given values:
            label: The value associated with this node
            color: 0 if black, 1 if red
            parent: The parent to this node
            left: This node's left child
            right: This node's right child
        """
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    # Here are functions which are specific to red-black trees

    def rotate_left(self):
        r"""Rotate the subtree rooted at this node to the left and
        returns the new root to this subtree.
        Perfoming one rotation can be done in O(1).

        情景一：
                    0 -> self
                /      \
              -10      10
              / \     / \
            -20 -5   5  20

                 0
               /  \
              -10  5

                    10
                   /  \
                  0   20
                /  \
              -10  5
              / \
            -20 -5

        情景二：

                    0
                /      \
              -10      10 -> self
              / \     / \
            -20 -5   5  20

            20
           /
          10
         /
        5

               0
            /    \
          -10    20
          / \    /
        -20 -5  10
                /
                5

        """
        parent = self.parent
        right = self.right
        self.right = right.left
        if self.right:
            self.right.parent = self
        self.parent = right
        right.left = self
        if parent is not None:
            if parent.left == self:
                parent.left = right
            else:
                parent.right = right
        right.parent = parent
        return right

    def rotate_right(self):
        r"""Rotate the subtree rooted at this node to the right and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).


                    10
                   /  \
                  0   20
                /  \
              -10  5
              / \
            -20 -5


                       0
                    /    \
                  -10    10
                 /  \    / \
               -20  -5  5  20


                   -10
                 /    \
                -20    0
                      / \
                     -5 10
                        / \
                        5 20



        """
        parent = self.parent
        left = self.left
        self.left = left.right
        if self.left:
            self.left.parent = self
        self.parent = left
        left.right = self
        if parent is not None:
            if parent.right is self:
                parent.right = left
            else:
                parent.left = left
        left.parent = parent
        return left

    def get_max(self):
        """Returns the largest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.right:
            # Go as far right as possible
            return self.right.get_max()
        else:
            return self.label

    def get_min(self):
        """Returns the smallest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.left:
            # Go as far left as possible
            return self.left.get_min()
        else:
            return self.label

    @property
    def grandparent(self):
        """Get the current node's grandparent, or None if it doesn't exist."""
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    @property
    def sibling(self):
        """Get the current node's sibling, or None if it doesn't exist."""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def is_left(self):
        """Returns true iff this node is the left child of its parent."""
        return self.parent and self.parent.left is self

    def is_right(self):
        """Returns true iff this node is the right child of its parent."""
        return self.parent and self.parent.right is self

    def __bool__(self):
        return True

    def __len__(self):
        """
        Return the number of nodes in this tree.
        """
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        return ln

    def __eq__(self, other):
        """Test if two trees are equal."""
        if self.label == other.label:
            return self.left == other.left and self.right == other.right
        else:
            return False

    def __repr__(self):
        from pprint import pformat

        if self.left is None and self.right is None:
            return "'%s %s'" % (self.label, (self.color and "red") or "blk")
        return pformat(
            {
                "%s %s"
                % (self.label, (self.color and "red") or "blk"): (self.left, self.right)
            },
            indent=1,
        )

    def preorder_traverse(self):
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()

    def inorder_traverse(self):
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()

    def postorder_traverse(self):
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label

    def __contains__(self, label):
        """Search through the tree for label, returning True iff it is
        found somewhere in the tree.
        Guaranteed to run in O(log(n)) time.
        """
        return self.search(label) is not None

    def search(self, label):
        """Search through the tree for label, returning its node if
        it's found, and None otherwise.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self
        elif label > self.label:
            if self.right is None:
                return None
            else:
                return self.right.search(label)
        else:
            if self.left is None:
                return None
            else:
                return self.left.search(label)

    def insert(self, label):
        print('&&&&&&& self: %s' % self)
        print('&&&&&&& label: %s' % label)
        """Inserts label into the subtree rooted at self, performs any
        rotations necessary to maintain balance, and then returns the
        new root to this subtree (likely self).
        This is guaranteed to run in O(log(n)) time.
        """
        if self.label is None:
            # Only possible with an empty tree
            self.label = label
            return self

        if label == self.label:
            print('label == self.label')
            return self
        elif label < self.label:
            print('label < self.label')
            print('self.left: %s' % self.left)
            if self.left:
                self.left.insert(label)
            else:
                self.left = RedBlackTree(label, 1, self)
                print('self.left: %s' % self.left)
                self.left._insert_repair()
        else:  # label > self.label
            print('label > self.label')
            print('self.right: %s' % self.right)
            if self.right:
                self.right.insert(label)
            else:
                self.right = RedBlackTree(label, 1, self)
                print('self.right: %s' % self.right)
                self.right._insert_repair()

        return self.parent or self

    def _insert_repair(self):
        """Repair the coloring from inserting into a tree."""
        if self.parent is None:
            # This node is the root, so it just needs to be black
            self.color = 0
        elif color(self.parent) == 0:
            # If the parent is black, then it just needs to be red
            self.color = 1
        else:  # 有父节点，父节点是红色
            uncle = self.parent.sibling
            if color(uncle) == 0:
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    self.right._insert_repair()
                elif self.is_right() and self.parent.is_left():
                    self.parent.rotate_left()
                    self.left._insert_repair()
                elif self.is_left():
                    self.grandparent.rotate_right()
                    self.parent.color = 0
                    self.parent.right.color = 1
                else:
                    self.grandparent.rotate_left()
                    self.parent.color = 0
                    self.parent.left.color = 1
            else:
                self.parent.color = 0
                uncle.color = 0
                self.grandparent.color = 1
                self.grandparent._insert_repair()

    ###################################################################################

    def remove(self, label):
        print('&&&&&&& self: %s' % self)
        print('&&&&&&& label: %s' % label)
        """Remove label from this tree."""
        if label == self.label:
            print('label == self.label')
            if self.left and self.right:
                print('self.left is not None and self.right is not None')
                # It's easier to balance a node with at most one child,
                # so we replace this node with the greatest one less than
                # it and remove that.
                value = self.left.get_max()
                print('value: %s' % value)
                self.label = value
                self.left.remove(value)
            else:
                # This node has at most one non-None child, so we don't
                # need to replace
                print('not self.left is not None and self.right is not None')
                print('self.color: %s' % self.color)
                if self.color == 1:
                    # This node is red, and its child is black
                    # The only way this happens to a node with one child
                    # is if both children are None leaves.
                    # We can just remove this node and call it a day.
                    if self.is_left():
                        self.parent.left = None
                    else:
                        self.parent.right = None
                else:
                    child = self.left or self.right
                    print('child: %s' % child)
                    # The node is black
                    if child is None:
                        print('没有左子树，也没有右子树')
                        # This node and its child are black
                        if self.parent is None:
                            # The tree is now empty
                            return RedBlackTree(None)
                        else:
                            self._remove_repair()
                            if self.is_left():
                                self.parent.left = None
                            else:
                                self.parent.right = None
                            self.parent = None
                    else:
                        print('有左子树，或者有右子树')
                        # This node is black and its child is red
                        # Move the child node here and make it black
                        r"""
                        有左子树
                          A -> self             B -> self
                         /             =>     /   \
                        B   -> child        None None
                        
                            A -> self          B -> self
                           /                  / \
                          B   -> child  =>   C   D
                         / \
                        C   D
                        
                        有右子树       
                        A   -> self            B -> self
                         \             =>    /   \
                          B -> child       None None
                        
                        A   -> self            B -> self
                         \                    / \
                          B -> child    =>   C   D
                         / \
                        C   D
                                
                        """
                        self.label = child.label
                        self.left = child.left
                        self.right = child.right
                        if self.left:
                            self.left.parent = self
                        if self.right:
                            self.right.parent = self
        elif label < self.label:
            print('label < self.label')
            if self.left:
                self.left.remove(label)
        else:  # label > self.label
            print('label > self.label')
            if self.right:
                self.right.remove(label)
        return self.parent or self

    def _remove_repair(self):
        r"""Repair the coloring of the tree that may have been messed up.
              A
             /
           B-0  ->self
          /  \
        None None

           A
            \
           B-0  ->self
          /  \
        None None
        """

        r"""self 兄弟节点为并且为红
              A           A-1        S-0
             / \          / \         /
           B-0 S-1  =>  B-0 S-0      A-1
          /  \                       /
        None None                   B-0

           A               A-1       S-0
          / \             /  \         \
        S-1 B-0     =>   S-0 B-0       A-1
            /  \                         \
          None None                      B-0
        """
        if color(self.sibling) == 1:
            self.sibling.color = 0
            self.parent.color = 1
            if self.is_left():
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()

        r"""
        父节点肯定有，并且为黑，
        根据后续处理一定有兄弟节点，并且兄弟节点为黑，
        但兄弟节点的左右子节点要么为黑，要么不存在
        
              A-0           A-0
             /   \         /   \
           B-0  S-0  =>  B-0  S-1
          /  \          /   \
        None None      None None
        
           A-0              A-0
          /  \             /  \
        S-0  B-0     =>  S-1  B-0
             /  \             /  \
           None None        None None
           
        """
        if (
            color(self.parent) == 0
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent._remove_repair()
            return

        r"""
        父节点肯定有，并且为红，
        根据后续处理一定有兄弟节点，并且兄弟节点为黑，
        但兄弟节点的左右子节点要么为黑，要么不存在

              A-1           A-0
             /   \         /   \
           B-0  S-0  =>  B-0  S-1
          /  \          /   \
        None None      None None

           A-1              A-0
          /  \             /  \
        S-0  B-0     =>  S-1  B-0
             /  \             /  \
           None None        None None

        """
        if (
            color(self.parent) == 1
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent.color = 0
            return

        r"""
        
                  A                      A                       A
             /       \                 /    \                  /    \
           B-0       S-0      =>      B-0   C-1    =>         B-0   C-0
          /  \      /   \            /   \    \              /   \    \
        None None C-1 为黑或者没有   None None  S-0          None None  S-1
                                                \                      \
                                             为黑或者没有                为黑或者没有
        """
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 0
            and color(self.sibling.left) == 1
        ):
            self.sibling.rotate_right()
            self.sibling.color = 0
            self.sibling.right.color = 1

        r"""
                      A
                 /        \
                S-0       B-0
              /    \      /  \
        为黑或者没有 C-1   None None
        
                 A
              /     \
            C-1    B-0
             /    /   \
           S-0  None None
           /
        为黑或者没有

                 A
              /     \
            C-0    B-0
             /    /   \
           S-1  None None
           /
        为黑或者没有
        
        """
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
            and color(self.sibling.left) == 0
        ):
            self.sibling.rotate_left()
            self.sibling.color = 0
            self.sibling.left.color = 1

        r"""
                    G
                   /
                  A
             /       \
           B-0       S-0
          /  \         \
        None None      C-1
        """
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
        ):
            self.parent.rotate_left()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0

        r"""
                        G
                       /
                      A
                 /        \
                S-0       B-0
              /           /  \
             C-1        None None
        """
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.left) == 1
        ):
            self.parent.rotate_right()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0

    def check_color_properties(self):
        """Check the coloring of the tree, and return True iff the tree
        is colored in a way which matches these five properties:
        (wording stolen from wikipedia article)
         1. Each node is either red or black.
         2. The root node is black.
         3. All leaves are black.
         4. If a node is red, then both its children are black.
         5. Every path from any node to all of its descendent NIL nodes
            has the same number of black nodes.
        This function runs in O(n) time, because properties 4 and 5 take
        that long to check.
        """
        # I assume property 1 to hold because there is nothing that can
        # make the color be anything other than 0 or 1.

        # Property 2
        if self.color:
            # The root was red
            print("Property 2")
            return False

        # Property 3 does not need to be checked, because None is assumed
        # to be black and is all the leaves.

        # Property 4
        if not self.check_coloring():
            print("Property 4")
            return False

        # Property 5
        if self.black_height() is None:
            print("Property 5")
            return False
        # All properties were met
        return True

    def check_coloring(self):
        """A helper function to recursively check Property 4 of a
        Red-Black Tree. See check_color_properties for more info.
        """
        if self.color == 1:
            if color(self.left) == 1 or color(self.right) == 1:
                return False
        if self.left and not self.left.check_coloring():
            return False
        if self.right and not self.right.check_coloring():
            return False
        return True

    def black_height(self):
        """Returns the number of black nodes from this node to the
        leaves of the tree, or None if there isn't one such value (the
        tree is color incorrectly).
        """
        if self is None:
            # If we're already at a leaf, there is no path
            return 1
        left = RedBlackTree.black_height(self.left)
        right = RedBlackTree.black_height(self.right)
        if left is None or right is None:
            # There are issues with coloring below children nodes
            return None
        if left != right:
            # The two children have unequal depths
            return None
        # Return the black depth of children, plus one if this node is
        # black
        return left + (1 - self.color)

    # Here are functions which are general to all binary search trees

    def floor(self, label):
        """Returns the largest element in this tree which is at most label.
        This method is guaranteed to run in O(log(n)) time."""
        if self.label == label:
            return self.label
        elif self.label > label:
            if self.left:
                return self.left.floor(label)
            else:
                return None
        else:
            if self.right:
                attempt = self.right.floor(label)
                if attempt is not None:
                    return attempt
            return self.label

    def ceil(self, label):
        """Returns the smallest element in this tree which is at least label.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self.label
        elif self.label < label:
            if self.right:
                return self.right.ceil(label)
            else:
                return None
        else:
            if self.left:
                attempt = self.left.ceil(label)
                if attempt is not None:
                    return attempt
            return self.label


def color(node):
    """Returns the color of a node, allowing for None leaves."""
    if node is None:
        return 0
    else:
        return node.color  # color: 0 if black, 1 if red


def test_insert_delete():
    r"""
    [0, -12, 8, -8, 15, 4, 12, 10, 9, 11]

    0-0 -> tree

    ********* insert -12 *********
    &&&&&&& self: '0 blk'
    &&&&&&& label: -12
    label < self.label
    self.left: None
    self.left: '-12 red'

      0-0 -> tree
      /
    -12-1

    ********* insert 8 *********
    &&&&&&& self: {'0 blk': ('-12 red', None)}
    &&&&&&& label: 8
    label > self.label
    self.right: None
    self.right: '8 red'

        0-0 -> tree
       /  \
    -12-1 8-1

    ********* insert -8 *********
    &&&&&&& self: {'0 blk': ('-12 red', '8 red')}
    &&&&&&& label: -8
    label < self.label
    self.left: '-12 red'
    &&&&&&& self: '-12 red'
    &&&&&&& label: -8
    label > self.label
    self.right: None
    self.right: '-8 red'

        0-0 -> tree
       /  \
    -12-1 8-1
       \
     -8-1

    _insert_repair(-8)

        0-1
       /  \
    -12-0 8-0
       \
     -8-1

    _insert_repair(0)

        0-0
       /  \
    -12-0 8-0
       \
     -8-1

    ********* insert 15 *********
    &&&&&&& self: {'0 blk': ({'-12 blk': (None, '-8 red')}, '8 blk')}
    &&&&&&& label: 15
    label > self.label
    self.right: '8 blk'
    &&&&&&& self: '8 blk'
    &&&&&&& label: 15
    label > self.label
    self.right: None
    self.right: '15 red'

        0-0 -> tree
       /  \
    -12-0 8-0
       \   \
     -8-1  15-1

    _insert_repair(15)


    ********* insert 4 *********
    &&&&&&& self: {'0 blk': ({'-12 blk': (None, '-8 red')}, {'8 blk': (None, '15 red')})}
    &&&&&&& label: 4
    label > self.label
    self.right: {'8 blk': (None, '15 red')}
    &&&&&&& self: {'8 blk': (None, '15 red')}
    &&&&&&& label: 4
    label < self.label
    self.left: None
    self.left: '4 red'

          0-0 -> tree
       /      \
    -12-0     8-0
       \     /  \
     -8-1  4-1 15-1

    _insert_repair(4)


    ********* insert 12 *********
    &&&&&&& self: {'0 blk': ({'-12 blk': (None, '-8 red')}, {'8 blk': ('4 red', '15 red')})}
    &&&&&&& label: 12
    label > self.label
    self.right: {'8 blk': ('4 red', '15 red')}
    &&&&&&& self: {'8 blk': ('4 red', '15 red')}
    &&&&&&& label: 12
    label > self.label
    self.right: '15 red'
    &&&&&&& self: '15 red'
    &&&&&&& label: 12
    label < self.label
    self.left: None
    self.left: '12 red'

          0-0 -> tree
       /      \
    -12-0     8-0
       \     /  \
     -8-1  4-1 15-1
                /
              12-1

    _insert_repair(12)

          0-0
       /      \
    -12-0     8-1
       \     /  \
     -8-1  4-0 15-0
                /
              12-1

    _insert_repair(8)


    ********* insert 10 *********
    &&&&&&& self: {'0 blk': ({'-12 blk': (None, '-8 red')},
               {'8 red': ('4 blk', {'15 blk': ('12 red', None)})})}
    &&&&&&& label: 10
    label > self.label
    self.right: {'8 red': ('4 blk', {'15 blk': ('12 red', None)})}
    &&&&&&& self: {'8 red': ('4 blk', {'15 blk': ('12 red', None)})}
    &&&&&&& label: 10
    label > self.label
    self.right: {'15 blk': ('12 red', None)}
    &&&&&&& self: {'15 blk': ('12 red', None)}
    &&&&&&& label: 10
    label < self.label
    self.left: '12 red'
    &&&&&&& self: '12 red'
    &&&&&&& label: 10
    label < self.label
    self.left: None
    self.left: '10 red'

          0-0 -> tree
       /      \
    -12-0     8-1
       \     /  \
     -8-1  4-0 15-0
                /
              12-1
                /
              10-1

    _insert_repair(10)

       12-1
      /   \
    10-1 15-0

          0-0
       /      \
    -12-0     8-1
       \     /  \
     -8-1  4-0 12-0
               /  \
             10-1 15-1

    ********* insert 9 *********
    &&&&&&& self: {'0 blk': ({'-12 blk': (None, '-8 red')},
               {'8 red': ('4 blk', {'12 blk': ('10 red', '15 red')})})}
    &&&&&&& label: 9
    label > self.label
    self.right: {'8 red': ('4 blk', {'12 blk': ('10 red', '15 red')})}
    &&&&&&& self: {'8 red': ('4 blk', {'12 blk': ('10 red', '15 red')})}
    &&&&&&& label: 9
    label > self.label
    self.right: {'12 blk': ('10 red', '15 red')}
    &&&&&&& self: {'12 blk': ('10 red', '15 red')}
    &&&&&&& label: 9
    label < self.label
    self.left: '10 red'
    &&&&&&& self: '10 red'
    &&&&&&& label: 9
    label < self.label
    self.left: None
    self.left: '9 red'

          0-0 -> tree
       /      \
    -12-0     8-1
       \     /  \
     -8-1  4-0 12-0
               /  \
             10-1 15-1
              /
             9-1

    _insert_repair(9)

          0-0
       /      \
    -12-0     8-1
       \     /  \
     -8-1  4-0 12-1
               /  \
             10-0 15-0
              /
             9-1

    _insert_repair(12)

        8-1
      /   \
    0-0  12-1
      \
     4-0

             8-1
          /       \
        0-0       12-1
       /   \     /   \
    -12-0 4-0  10-0 15-0
      \         /
    -8-1       9-1

             8-0
          /       \
        0-1       12-1
       /   \     /   \
    -12-0 4-0  10-0 15-0
      \         /
    -8-1       9-1



    ********* insert 11 *********
    &&&&&&& self: {'8 blk': ({'0 red': ({'-12 blk': (None, '-8 red')}, '4 blk')},
               {'12 red': ({'10 blk': ('9 red', None)}, '15 blk')})}
    &&&&&&& label: 11
    label > self.label
    self.right: {'12 red': ({'10 blk': ('9 red', None)}, '15 blk')}
    &&&&&&& self: {'12 red': ({'10 blk': ('9 red', None)}, '15 blk')}
    &&&&&&& label: 11
    label < self.label
    self.left: {'10 blk': ('9 red', None)}
    &&&&&&& self: {'10 blk': ('9 red', None)}
    &&&&&&& label: 11
    label > self.label
    self.right: None
    self.right: '11 red'

               8-0
          /          \
        0-1         12-1
       /   \       /   \
    -12-0 4-0    10-0 15-0
      \         /   \
    -8-1       9-1 11-1

                                   8-0
                    /                                 \
                  0-1                                12-1
            /             \                     /             \
        -12-0            4-0                  10-0            15-0
      /      \         /      \          /           \       /    \
    NULL-0   -8-1    NULL-0 NULL-0     9-1           11-1  NULL-0 NULL-0
            /   \                    /    \         /    \
        NULL-0 NULL-0              NULL-0 NULL-0  NULL-0 NULL-0

    1）每个结点要么是红的，要么是黑的。
    2）根结点是黑的。
    3）每个叶结点（叶结点即指树尾端NIL指针或NULL结点）是黑的。
    4）如果一个结点是红的，那么它的俩个儿子都是黑的。
    5）对于任一结点而言，其到叶结点树尾端NIL指针的每一条路径都包含相同数目的黑结点。

    """
    tree = RedBlackTree(0)

    for i in [-12, 8, -8, 15, 4, 12, 10, 9, 11]:
        print('********* insert %s *********' % i)
        tree = tree.insert(i)

    r"""
    
               8-0
          /          \
        0-1         12-1
       /   \       /   \
    -12-0 4-0    10-0 15-0
      \         /   \
    -8-1       9-1 11-1

    
    [15, -12, 9]
    
    ********* delete 15 *********
    &&&&&&& self: {'8 blk': ({'0 red': ({'-12 blk': (None, '-8 red')}, '4 blk')},
               {'12 red': ({'10 blk': ('9 red', '11 red')}, '15 blk')})}
    &&&&&&& label: 15
    &&&&&&& self: {'12 red': ({'10 blk': ('9 red', '11 red')}, '15 blk')}
    &&&&&&& label: 15
    &&&&&&& self: '15 blk'
    &&&&&&& label: 15
    child: None
    {'8 blk': ({'0 red': ({'-12 blk': (None, '-8 red')}, '4 blk')},
               {'10 red': ('9 blk', {'12 blk': ('11 red', None)})})}
    ********* delete -12 *********
    &&&&&&& self: {'8 blk': ({'0 red': ({'-12 blk': (None, '-8 red')}, '4 blk')},
               {'10 red': ('9 blk', {'12 blk': ('11 red', None)})})}
    &&&&&&& label: -12
    &&&&&&& self: {'0 red': ({'-12 blk': (None, '-8 red')}, '4 blk')}
    &&&&&&& label: -12
    &&&&&&& self: {'-12 blk': (None, '-8 red')}
    &&&&&&& label: -12
    child: '-8 red'
    {'8 blk': ({'0 red': ('-8 blk', '4 blk')},
               {'10 red': ('9 blk', {'12 blk': ('11 red', None)})})}
    ********* delete 9 *********
    &&&&&&& self: {'8 blk': ({'0 red': ('-8 blk', '4 blk')},
               {'10 red': ('9 blk', {'12 blk': ('11 red', None)})})}
    &&&&&&& label: 9
    &&&&&&& self: {'10 red': ('9 blk', {'12 blk': ('11 red', None)})}
    &&&&&&& label: 9
    &&&&&&& self: '9 blk'
    &&&&&&& label: 9
    child: None
    {'8 blk': ({'0 red': ('-8 blk', '4 blk')}, {'11 red': ('10 blk', '12 blk')})}

    """
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    for i in [15, -12, 9]:
        print('********* delete %s *********' % i)
        tree = tree.remove(i)
        print(tree)



    if not tree.check_color_properties():
        return False
    if list(tree.inorder_traverse()) != [-8, 0, 4, 8, 10, 11, 12]:
        return False
    return True


if __name__ == '__main__':
    print(test_insert_delete())