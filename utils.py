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
