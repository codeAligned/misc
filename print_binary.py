#!/usr/bin/python

# Printing Binary Trees
# By: Steve Krenzel

# http://stevekrenzel.com/articles/printing-trees
# Sometimes when debugging trees it's useful to analyze them by printing them out. Using a reversed inorder traversal makes this easy.
# Using the code below you'll get something like this:



class BinaryTree:
    def __init__(self, depth, value=0):
        self.value = value
        # For demo purposes, this just creates a full binary tree
        self.left  = BinaryTree(depth-1, value*2 + 1) if depth > 0 else None
        self.right = BinaryTree(depth-1, value*2 + 2) if depth > 0 else None

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.value)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret

if __name__ == "__main__":
    print BinaryTree(4)