import numpy as np
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

# Calculate entropy of distribution p: H(p) = -(p_1 * log(p_1) + ... p_n * log(p_n))
def entropy(source):
    n = len(source)
    res = 0
    for i in range(n):
        res -= source[i].prob * np.log2(source[i].prob)
    return res

def mean_codeword_length(source):
    n = len(source)
    res = 0
    for i in range(n):
        res += source[i].prob * len(source[i].code)
    return res

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

def kraft_encode(source):
    lengths = []
    max_length = 0
    n = len(source)
    
    # calculate expected length of each @source character
    for i in range(n):
        new_length = - np.log2(source[i].prob)
        new_length = int(np.ceil(new_length))
        lengths.append(new_length)
        max_length = max(max_length, new_length)
    
    # store all leaves at height @max_length of coding tree
    leaves = ['']
    for k in range(max_length):
        new_leaves = []
        for leaf in leaves:
            new_leaves.append(leaf + '0')
            new_leaves.append(leaf + '1')
        leaves = new_leaves

    # calculate Kraft's code for @source
    block_start = 0
    for i in range(n):
        # codeword for @source[i]
        source[i].code = leaves[block_start][0:lengths[i]]
        # go to next block
        block_start += int(pow(2, max_length - lengths[i]))
    return source

def huffman_encode(source):
    tree_nodes = []
    for item in source:
        new_node = TreeNode("", char = item)
        tree_nodes.append(new_node)

    # build structure of Huffman Tree
    while (len(tree_nodes) > 1):
        # remove two node with smallest probability
        tree_nodes.sort(key = lambda x: -x.char.prob)
        x = tree_nodes[-1]
        y = tree_nodes[-2]
        tree_nodes = tree_nodes[:-2]
        # create new node
        new_val = x.char.val + y.char.val
        new_prob = x.char.prob + y.char.prob
        new_char = character(new_val, new_prob)
        new_tree_node = TreeNode("", new_char, children = [x, y])
        # add new node which probability = P(x) + P(y)
        tree_nodes.append(new_tree_node)
        
    # get Huffman code from builded coding tree
    root = tree_nodes[0]
    label_coding_tree(root)
    result_code = get_code_from_coding_tree(root)
    return result_code
        

# def tunstall_code(source):

# def lempel_ziv_code(source):


if __name__ == '__main__':
    source = [character('a', 0.5), character('b', 0.3), character('c', 0.2)]

    print(f"Entropy: {entropy(source)}\n")

    print("Kraft code: ")
    code = kraft_encode(source)
    for elem in code:
        print(elem.val, elem.prob, elem.code)

    print(f"Mean codeword length: {mean_codeword_length(code)}\n")

    print("Huffman code: ")
    code = huffman_encode(source)
    for elem in code:
        print(elem.val, elem.prob, elem.code)

    print(f"Mean codeword length: {mean_codeword_length(code)}\n")
