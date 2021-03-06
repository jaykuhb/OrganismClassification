import fastaParser
import features
import numpy as np

# return set of lengths of given lists
def lengthSet(sequences):
    lengths = set()
    for seq in sequences:
        if not (len(seq) in lengths):
            lengths.add(len(seq))
    return lengths

def nonBaseCharCount(sequences):
    bases = ['a', 'c', 'g', 't']
    d = {}
    for seq in sequences:
        for s in seq:
            if s not in bases:
                if s not in d:
                    d[s]=1
                else:
                    d[s]+=1
    return d

seq = 'acacac'
print (seq[:-1])

print (seq)
f = features.fourier(seq,4)
print (features.fourier(seq,4))

print (np.fft.rfftfreq(len(seq)))
#print ("Feature test: triplets - ", seq)
#print (features.tripletsHist(seq))
#print ("Feature test: pairs - ", seq)
#print (features.pairHist(seq))

with open('current_Fungi_unaligned.fa') as fp:
    namesSeqMap = fastaParser.getNamesSeqSet(fp)
    print ("Parsed:", len(namesSeqMap), "species")

    sortedBySeqCount = sorted(namesSeqMap.items(), key=lambda x: len(x[1]), reverse = True)
    n  = 10
    print (n,"species containing most unique sequences:")

    i = 0
    for pair in sortedBySeqCount:
        print(pair[0], len(pair[1]))
        print (max(lengthSet(pair[1])))
        print (min(lengthSet(pair[1])))
        i+=1
        if i==n:
            break


   
    # stats for single species
    species = sortedBySeqCount[40]
    strangeChars = nonBaseCharCount(species[1])
    print ("Incomplete bases characters:")
    print (strangeChars)

    lengths = lengthSet(species[1])
    print (len(lengths))
    #print(lengths)

    species = sortedBySeqCount[50]
    lengths = lengthSet(species[1])
    print (len(lengths))
    #print(lengths)
"""
    trigrams = []
    i =0
    for seq in kind[1]:
        tmp = pairHist(seq)
        trigrams.append(tmp)
        print (tmp)
        i+=1
        if i == n:
            break
"""