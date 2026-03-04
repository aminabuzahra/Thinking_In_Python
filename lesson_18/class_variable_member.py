class Tree:
    number_of_trees = 0

    def __init__(self):
        # Tree.number_of_trees = Tree.number_of_trees + 1
        Tree.number_of_trees += 1

    def print_number_of_trees(self):
        print(Tree.number_of_trees)

tree = Tree()
tree = Tree()
tree = Tree()
tree = Tree()
tree = Tree()

tree.print_number_of_trees()
