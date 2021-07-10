import numpy as np

class elem:
    def __init__(self, char, p, code = None):
        self.char = char
        self.p = p
        self.code = code

'''Calculate entropy of distribution p: H(p) = -(p_1 * log(p_1) + ... p_n * log(p_n))'''
def entropy(p):
    res = 0
    n = len(p) # number of element in p

    for i in range(n):
        res -= p[i].p * np.log2(p[i].p)

    return res

'''Calculate cross entropy between p and q: H(p; q) = -(p_1 * log(q_1) + ... p_n * log(q_n))'''
def cross_entropy(p, q):
    res = 0
    n = len(p) # number of element in p (or q)

    for i in range(n):
        res -= p[i].p * np.log2(q[i].p)

    return res

def mean_codeword_length(p):
    res = 0
    n = len(p) # number of element in p (or q)

    for i in range(n):
        res += p[i].p * len(p[i].code)

    return res

#def kraft_code(p):


if __name__ == '__main__':
    p = [elem('a', 0.5, "0"), elem('b', 0.3, "10"), elem('c', 0.2, "110")]
    q = [elem('a', 0.4), elem('b', 0.3), elem('c', 0.3)]
    print(f"Entropy: {entropy(p)}")
    print(f"Cross entropy: {cross_entropy(p, q)}")
    print(f"Mean codeword length: {mean_codeword_length(p)}")
