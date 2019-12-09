#This script includes implementations of the FormationTree and PermutationVector algorithms for computing formation width, as well as: 
#code for comparing the run time of FormationTree and PermutationVector on sequences of form (a b c ..)^t, 
#code to generate all 3-letter sequences of formation width x and alternation length x+1 for x = 5, 6, 7, 8 using PermutationVector

from itertools import permutations
import time
import random
import numpy as np
import timeit

#determines whether one sequence is a subsequence of another:
def issubseq(seq, subseq):
    if len(subseq) == 0:
        return True
    else:
        if len(seq) == 0:
            return False
        elif seq[-1] == subseq[-1]:
            return issubseq(seq[:-1],subseq[:-1])
        elif seq[-1] != subseq[-1]:
            return issubseq(seq[:-1],subseq)

#determines the formation width of u using FormationTree:
def fw(u):
    l=len(set(u))
    v = list(u)
    rsformset = set()
    rsformset1 = set()
    q = tuple(range(l))
    q1 = q[::-1]
    rsformset.add(q)
    rsform1=q
    while len(rsformset)!=0:
        for rsforms in rsformset:
            done=False
            for perms in permutations(range(l)):
                for i in range(len(u)):
                    v[i] = perms[u[i]]
                if issubseq(rsforms, v):
                    done=True
                    break
            if not done:
                rsformset1.add(rsforms+q)
                rsformset1.add(rsforms+q1)
                rsform1=rsforms+q
        rsformset.clear()
        for rsform in rsformset1:
            rsformset.add(rsform)
        rsformset1.clear()
    return len(rsform1)//l

#determines the formation width of u using PermutationVector:
def nfw(u):
    lu = len(u) #calc len(u) once
    if lu == 0:
        return 0
    s = 1
    l=len(set(u))
    perml = set() #set of permutations:
    for perms in permutations(range(l)):
        perml.add(perms)
    lenperml = len(perml)
    v = {}
    rsformset = set() #set of permutation vectors
    rsformset1 = set()
    q = tuple(range(l))
    q1 = q[::-1]
    qdata = ()
    for perms in perml: #make dictionary of subsequences isomorphic to u
        v[perms] = {}
        for i in range(lu):
            v[perms][i] = perms[u[i]]
        start = 0
        usegi = 0
        check = 0
        for i in range(lu): #find longest initial segment of each perm of u in root formation
            check = 0
            for j in range(start, l):
                if j == v[perms][i]:
                    start = j+1
                    usegi = i+1
                    check = 1
                    break
            if check == 0:
                break
        qdata = qdata + ((perms,usegi),)
    checker = 0
    for i in range(lenperml):
        if qdata[i][1] == lu:
            checker = 1
    if checker == 0: #if the root formation contained no perm of u
        rsformset.add(qdata)
    counter = 0
    while len(rsformset)!=0: #make a tree of permutation vectors
        counter += 1
        s += 1
        for rsforms in rsformset: #the permutation vectors in the current level of the tree
            qdata = ()
            qdata1 = ()
            for perms in perml:
                for i in range(lenperml):
                    if rsforms[i][0] == perms:
                        ustart = rsforms[i][1]
                start = 0
                usegi = 0
                check = 0
                for i in range(ustart, lu): #find longest initial segment of each perm of u in formation obtained by adding increasing perm
                    check = 0
                    for j in range(start, l):
                        if j == v[perms][i]:
                            start = j+1
                            usegi = i+1
                            check = 1
                            break
                    if check == 0:
                        break
                qdata = qdata + ((perms,usegi),) #a new permutation vector in the next level of the tree
                        
                start = l-1
                #print('*')
                for i in range(ustart, lu): #find longest initial segment of each perm of u in formation obtained by adding decreasing perm
                    check = 0
                    for j in range(start, -1,-1):
                        if j == v[perms][i]:
                            start = j-1
                            usegi = i+1
                            check = 1
                            break
                    if check == 0:
                        break
                qdata1 = qdata1 + ((perms,usegi),) #a new permutation vector in the next level of the tree   
                        
            checker = 0
            for i in range(lenperml):
                if qdata[i][1] == lu:
                    checker = 1
            if checker == 0: #if the formation corresponding to the permutation vector contained no perm of u
                rsformset1.add(qdata)
            
            checker = 0
            for i in range(lenperml):
                if qdata1[i][1] == lu:
                    checker = 1
            if checker == 0: #if the formation corresponding to the permutation vector contained no perm of u
                rsformset1.add(qdata1)
                
        rsformset.clear()
        for rsform in rsformset1:
            rsformset.add(rsform)
        rsformset1.clear()
        
    return s

#example of computing old and new formation width algorithm on an arbitrary 3-letter sequence
t0 = time.time()
print(fw([0,1,2,2,1,0,0,1,2,2,1,0,1,1,2,2,1,0,0,1,2,2,1,0,1]))
t1 = time.time()
total = t1-t0
print(total)
t0 = time.time()
print(nfw([0,1,2,2,1,0,0,1,2,2,1,0,1,1,2,2,1,0,0,1,2,2,1,0,1]))
t1 = time.time()
total = t1-t0
print(total)

#comparison of run-times for FormationTree vs PermutationVector on (a b c ..)^t sequences
for i in [3,4]:
    print('')
    for j in range(1,11):
        upp = []
        for q in range(i):
            upp.append(q)
        seq = upp
        for x in range(1, j):
            seq = seq + upp
        #print(seq)
        rt_old = []
        rt_new = []
        t0 = time.perf_counter()
        for t in range(20):
            ans = fw(seq)
        t1 = time.perf_counter()
        rt_old = round((t1-t0)/20.0,6)
        t0 = time.perf_counter()
        for t in range(20):
            ans = nfw(seq)
        t1 = time.perf_counter()
        rt_new = round((t1-t0)/20.0,6)
        #print(rt_old)
        #print(rt_new)
        #print(rt_old)
        #print(rt_new)
        print(str((i, j)),' & ',rt_old,' & ',rt_new,' \\\ ')

#computations for listing 3-letter sequences of formation width x and alternation length x+1 in appendix of paper
seq3 = {}
for i in range(1,14):
    if i == 1:
        seq3[i] = [[0,],]
    if i > 1:
        seq3[i] = []
        for j in seq3[i-1]:
            maxl = 0
            for q in j:
                maxl = max(maxl, q)
            if maxl == 0:
                j1 = j.copy()
                j2 = j.copy()
                j1.append(0)
                j2.append(1)
                seq3[i].append(j1)
                seq3[i].append(j2)
            else:
                j1 = j.copy()
                j2 = j.copy()
                j3 = j.copy()
                j1.append(0)
                j2.append(1)
                j3.append(2)
                seq3[i].append(j1)
                seq3[i].append(j2)
                seq3[i].append(j3)


                
for i in range(6,10):
    print('')
    print(i)
    print('')
    alt = {}
    alt[(0,1)] = [0,1,0,1,0,1]
    up = [0,1,2,0,1,2,0,1,2]
    for k in range(6, i):
        if k % 2 == 0:
            up.append(0)
            alt[(0,1)].append(0)
        else:
            up.append(1)
            up.append(2)
            alt[(0,1)].append(1)
    alt[(1,0)] = [1,0,1,0,1,0]
    for k in range(6, i):
        if k % 2 == 0:
            alt[(1,0)].append(1)
        else:
            alt[(1,0)].append(0)
    #print(i)
    alt[(2,1)] = [2,1,2,1,2,1]
    for k in range(6, i):
        if k % 2 == 0:
            alt[(2,1)].append(2)
        else:
            alt[(2,1)].append(1)
    alt[(1,2)] = [1,2,1,2,1,2]
    for k in range(6, i):
        if k % 2 == 0:
            alt[(1,2)].append(1)
        else:
            alt[(1,2)].append(2)
    alt[(0,2)] = [0,2,0,2,0,2]
    for k in range(6, i):
        if k % 2 == 0:
            alt[(0,2)].append(0)
        else:
            alt[(0,2)].append(2)
    alt[(2,0)] = [2,0,2,0,2,0]
    for k in range(6, i):
        if k % 2 == 0:
            alt[(2,0)].append(2)
        else:
            alt[(2,0)].append(0)
    t0 = time.time()
    if i%2 == 0:
        q = int(3*i / 2)
    else:
        q = int((3*(i-1) / 2)+1)
    for qi in range(1,q+1):
        for j in seq3[qi]:
            if nfw(j) == i-1 and (issubseq(j, alt[(0,1)]) or issubseq(j, alt[(1,0)]) or issubseq(j, alt[(2,0)]) or issubseq(j, alt[(0,2)]) or issubseq(j, alt[(2,1)]) or issubseq(j, alt[(1,2)])):
                strj = ''
                for r in range(len(j)):
                    strj = strj+str(j[r])
                print(strj)
    t1 = time.time()
    total = t1-t0
    print(total)