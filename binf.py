import itertools

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

lst = list(itertools.product([0, 1], repeat=4))
subforms = []
for j in lst:
    seq = []
    for t in range(len(j)):
        if j[t] == 1:
            seq = seq+[0,1,2]
        else:
            seq = seq+[2,1,0]
    subforms.append(seq)

for seq in subforms: # (a b c)^t b a c a b c
    if issubseq(seq, [1,0,2,0,1,2]) or issubseq(seq, [0,2,1,0,1,2,0]) or issubseq(seq, [0,1,0,2,1,2,0,1]) or issubseq(seq, [2,1,0,1,2,0,2,1,0]) or issubseq(seq, [2,1,0,2,0,1,2,1,0,2]) or issubseq(seq, [2,1,0,2,1,2,0,1,0,2,1]):
        print('*')
    else:
        print(seq)
print('')
        
for seq in subforms: # (a b c)^t b a c b a c
    if issubseq(seq, [1,0,2,1,0,2]) or issubseq(seq, [0,2,1,0,2,1,0]) or issubseq(seq, [0,1,0,2,1,0,2,1]) or issubseq(seq, [2,1,0,1,2,0,1,2,0]) or issubseq(seq, [2,1,0,2,0,1,2,0,1,2]) or issubseq(seq, [2,1,0,2,1,2,0,1,2,0,1]):
        print('*')
    else:
        print(seq)
print('')
        
for seq in subforms: # (a b c)^t a c b a c b
    if issubseq(seq, [0,2,1,0,2,1]) or issubseq(seq, [0,1,0,2,1,0,2]) or issubseq(seq, [0,1,2,1,0,2,1,0]) or issubseq(seq, [2,1,0,2,0,1,2,0,1]) or issubseq(seq, [2,1,0,2,1,2,0,1,2,0]) or issubseq(seq, [2,1,0,2,1,0,1,2,0,1,2]):
        print('*')
    else:
        print(seq)

print('')

for seq in subforms: # (a b c)^t a c b a b c
    if issubseq(seq, [0,2,1,0,1,2]) or issubseq(seq, [0,1,0,2,1,2,0]) or issubseq(seq, [0,1,2,1,0,2,0,1]) or issubseq(seq, [2,1,0,2,0,1,2,1,0]) or issubseq(seq, [2,1,0,2,1,2,0,1,0,2]) or issubseq(seq, [2,1,0,2,1,0,1,2,0,2,1]):
        print('*')
    else:
        print(seq)
        
print('')

for seq in subforms: # (a b c)^{t+1} a c b
    if issubseq(seq, [0,1,2,0,2,1]) or issubseq(seq, [0,1,2,0,1,0,2]) or issubseq(seq, [0,1,2,0,1,2,1,0]) or issubseq(seq, [2,1,0,2,1,0,2,0,1]) or issubseq(seq, [2,1,0,2,1,0,2,1,2,0]) or issubseq(seq, [2,1,0,2,1,0,2,1,0,1,2]):
        print('*')
    else:
        print(seq)