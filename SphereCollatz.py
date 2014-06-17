import sys

#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

cache = [-1] * 1000000 

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """

    # checking argument validity 
    assert type(i) is int 
    assert type(j) is int 

    # checking pre-conditions 
    assert i>=1 

    # my code 
    out = 0 
    if(i<j):
        low,high = i,j 
    else: 
        low,high = j,i 

    # checking for the b<m rule 
    m = high//2 
    if(low<m):
        return collatz_eval(m,high) 

    for k in range(low,high+1):
        if(cache[k]!=-1): 
            steps = cache[k] 
        else:
            key = k
            steps = 1
            while(k>1): 
                if(k%2==0): 
                    k = k//2 
                    steps += 1
                else: 
                    # taking two steps if odd 
                    k = k+(k>>1)+1 
                    steps += 2 
            cache[key] = steps 

        if(steps>out): 
            out = steps

    # checking post conditions 
    assert type(out) is int 

    # checking return conditions 
    assert out>=0 

    return out

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)


# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)