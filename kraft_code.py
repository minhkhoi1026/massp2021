from utils import *
from coding_tree import *

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

if __name__ == '__main__':
    source = [character('a', 0.5), character('b', 0.3), character('c', 0.2)]

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
