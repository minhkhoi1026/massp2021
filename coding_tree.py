from anytree import RenderTree, NodeMixin

class character:
    def __init__(self, val, prob, code = None):
        self.val = val
        self.prob = prob
        self.code = code

class TreeNode(NodeMixin):  # Add Node feature
     def __init__(self, name, char, parent=None, children=None):
        self.name = name
        self.char = char
        self.parent = parent
        if children:  # set children only if given
            self.children = children
# label each node in coding tree with codeword
def label_coding_tree(root):
    # if root is leaf then return
    if (len(root.children) == 0):
        return
    # if root is not leaf then for each child of root label name of that child
    # and its subtree
    c = 0
    for child in root.children:
        child.name = root.name + str(c)
        label_coding_tree(child)
        c += 1

# get code from all leaves of tree
def get_code_from_coding_tree(root):
    # if root is leaf then add value of root into result code
    if (len(root.children) == 0):
        root.char.code = root.name
        result_code = [root.char]
        return result_code
    # if root not leaf then return all result from root's subtree
    result_code = []
    for child in root.children:
        result_code.extend(get_code_from_coding_tree(child))
    return result_code
