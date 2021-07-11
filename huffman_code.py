from utils import *
from coding_tree import *

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

if __name__ == '__main__':
    source = [character('a', 0.5), character('b', 0.3), character('c', 0.2)]

    print("Huffman code: ")
    code = huffman_encode(source)
    for elem in code:
        print(elem.val, elem.prob, elem.code)

    print(f"Mean codeword length: {mean_codeword_length(code)}\n")