import numpy as np

class character:
    def __init__(self, char, prob, code = None):
        self.char = char
        self.prob = prob
        self.code = code

'''Calculate entropy of distribution p: H(p) = -(p_1 * log(p_1) + ... p_n * log(p_n))'''
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

def kraft_code(source):
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

# def huffman_code(source):

# def tunstall_code(source):

# def lempel_ziv_code(source):


if __name__ == '__main__':
    source = [character('a', 0.5), character('b', 0.3), character('c', 0.2)]

    print(f"Entropy: {entropy(source)}")

    print("Kraft code: ")
    kraft_code(source)
    for elem in source:
        print(elem.char, elem.prob, elem.code)

    print(f"Mean codeword length: {mean_codeword_length(source)}")
