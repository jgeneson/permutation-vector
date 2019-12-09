# permutation-vector
algorithm for computing fw(u) for sequences u

Generalized Davenport-Schinzel sequences are sequences that avoid a forbidden subsequence and have a sparsity requirement on their letters. Upper bounds on the lengths of generalized Davenport-Schinzel sequences have been applied to a number of problems in discrete geometry and extremal combinatorics. Sharp bounds on the maximum lengths of generalized Davenport-Schinzel sequences are known for some families of forbidden subsequences, but in general there are only rough bounds on the maximum lengths of most generalized Davenport-Schinzel sequences. One method that was developed for finding upper bounds on the lengths of generalized Davenport-Schinzel sequences uses a family of sequences called formations. 

An (r, s)-formation is a concatenation of s permutations of r distinct letters. The formation width function fw(u) is defined as the minimum s for which there exists r such that every (r, s)-formation contains u. The function fw(u) has been used with upper bounds on extremal functions of (r, s)-formations to find tight bounds on the maximum possible lengths of many families of generalized Davenport-Schinzel sequences. Algorithms have been found for computing fw(u) for sequences u of length n, but they have worst-case run time exponential in n, even for sequences u with only three distinct letters. We present an algorithm for computing fw(u) with run time O(n^{alpha_r}), where r is the number of distinct letters in u and alpha_r is a constant that only depends on r. We implement the new algorithm in Python (fwpv.py) and compare its run time to the next fastest algorithm for computing formation width. We also apply the new algorithm to find sharp upper bounds on the lengths of several families of generalized Davenport-Schinzel sequences with 3-letter forbidden patterns. The paper (pfw.pdf) explains more about the algorithm and its applications, and the other file (binf.py) is used in the proof of Proposition 3.2 in the paper.
