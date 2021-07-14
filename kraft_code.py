from utils import *
from coding_tree import *

# return Kraft code of @source
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
    leaves = get_all_binary_word_with_length(max_length)

    # calculate Kraft's code for @source
    block_start = 0
    for i in range(n):
        # codeword for @source[i]
        source[i].code = leaves[block_start][0:lengths[i]]
        # go to next block
        block_start += int(pow(2, max_length - lengths[i]))
    return source

if __name__ == '__main__':
    source = [character('A', 0.5), character('B', 0.2), character('C', 0.2), character('D', 0.1)]

    print("Kraft code: ")
    code = kraft_code(source)
    for elem in code:
        print(elem.val, elem.prob, elem.code)

    print(f"Mean codeword length: {mean_codeword_length(code)}\n")
