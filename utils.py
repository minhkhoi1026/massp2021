import numpy as np
from anytree import RenderTree, NodeMixin

# Calculate entropy of distribution p: H(p) = -(p_1 * log(p_1) + ... p_n * log(p_n))
def entropy(source):
    n = len(source)
    res = 0
    for i in range(n):
        res -= source[i].prob * np.log2(source[i].prob)
    return res

# Calculate mean codeword length of code
def mean_codeword_length(source):
    n = len(source)
    res = 0
    for i in range(n):
        res += source[i].prob * len(source[i].code)
    return res

# return list of all leaves at height @length of binary tree
def get_all_binary_word_with_length(length):
    leaves = ['']
    for k in range(length):
        new_leaves = []
        for leaf in leaves:
            new_leaves.append(leaf + '0')
            new_leaves.append(leaf + '1')
        leaves = new_leaves
    return leaves
