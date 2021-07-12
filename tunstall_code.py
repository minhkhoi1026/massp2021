from utils import *
from coding_tree import *
import numpy as np

# return tunstall code with length @b of @source
def tunstall_code(source, b):
    n = len(source)
    alpha = (np.power(2, b) - 1) // (n - 1)

    # init tree with @root represent empty character
    root = character("", prob = 1)
    leaf_nodes = [root]

    # build Tunstall coding tree
    for i in range(alpha):
        # remove leaf node @x with biggest probability
        leaf_nodes.sort(key = lambda x: -x.prob)
        x = leaf_nodes[0]
        leaf_nodes = leaf_nodes[1:]
        # add @n new leaf node to @x
        for j in range(n):
            new_val = x.val + source[j].val # w*x_i
            new_prob = x.prob * source[j].prob # P(w*x_i) = P(w) * P(x_i)
            new_char = character(new_val, new_prob)
            leaf_nodes.append(new_char)
    
    translate_codewords = get_all_binary_word_with_length(b)
    code = []
    for i in range(len(leaf_nodes)):
        leaf_nodes[i].code = translate_codewords[i]
    return leaf_nodes

if __name__ == '__main__':
    source = [character('a', 0.5), character('b', 0.3), character('c', 0.2)]

    print("Tunstall code: ")
    code = tunstall_code(source, 3)
    for elem in code:
        print(elem.val, elem.prob, elem.code)

    print(f"Mean codeword length: {mean_codeword_length(code)}\n")
