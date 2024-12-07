import sys
import numpy as np
import re
#### första delen


ordering={}
prints=[]

def check_ok(pages):
    for i in range(len(pages)):
        if pages[i] in ordering:
            before=ordering[pages[i]]
            for j in range(0, i):
                if pages[j] in before:
                    return False
    
    return True

def sort_print(page):
    for i in range(len(page)):
        if page[i] in ordering:
            before=ordering[page[i]]
            for j in range(0, i):
                if page[j] in before:
                    temp=page[j]
                    page[j]=page[i]
                    page[i]=temp
    




for line in sys.stdin:
    if '|' in line:
        vals = line.split('|')
        if int(vals[0]) in ordering:
            ordering[int(vals[0])].append( int(vals[1]))
        else:
            ordering[int(vals[0])]= [int(vals[1])]
    elif not line=='\n':
        vals=line.split(',')
        values=[]
        for v in vals:
            values.append(int(v))
        prints.append(values)
    
    

sum=0
for p in prints:
    if not check_ok(p):
        #print(p)
        sort_print(p)
        #print(p)
        mid=(len(p)-1)/2
        sum+= p[int(mid)]

print(sum)



