#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    return map(int, s.split())

# -------------
# cycle_length
# -------------

def cycle_length(n):
    """
    take int n
    evaluate the cycle length of the integer n
    return the computed cycle length
    """
    c = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        c += 1
    
    return c
    
#int cycle_length (int n) {
    #int count = 1;
    #while (n > 1) {
        #if (n % 2 == 0) // even
            #n = n /2;
        #else  {// odd
            #n = n + (n >> 1) + 1;
            #count += 1;
        #}
        #count += 1;
    #}
    #return count;
#}

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    return max([cycle_length(x) for x in range(i, j + 1)])

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
