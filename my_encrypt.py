import numpy as np

'''Calculate entropy of distribution p: H(p) = -(p_1 * log(p_1) + ... p_n * log(p_n))'''
def entropy(p):
    res = 0
    n = len(p) # number of element in p

    for i in range(n):
        res -= p[i] * np.log2(p[i])

    return res

'''Calculate cross entropy between p and q: H(p; q) = -(p_1 * log(q_1) + ... p_n * log(q_n))'''
def cross_entropy(p, q):
    res = 0
    n = len(p) # number of element in p (or q)

    for i in range(n):
        res -= p[i] * np.log2(q[i])

    return res

def mean_codeword_length(p, l):
    res = 0
    n = len(p) # number of element in p (or q)

    for i in range(n):
        res += p[i] * l[i]

    return res

if __name__ == '__main__':
    p = [0.5, 0.3, 0.2]
    q = [0.4, 0.3, 0.3]
    l = [1, 2, 3]
    print(f"Entropy: {entropy(p)}")
    print(f"Cross entropy: {cross_entropy(p, q)}")
    print(f"Mean codeword length: {mean_codeword_length(p, l)}")
