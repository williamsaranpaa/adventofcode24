import sys
import numpy as np
import itertools
#### första delen
operators=['+', '*']

values=[]
operands=[]

def add_or_mul(op, add, val):
    v=0
    for i in range (len(op)-1):
        
        if add[i]==0:
            if i==0:
                v=op[i]+op[i+1]
            else:
                v=v+op[i+1]

        elif add[i]==1:
            if i==0:
                v=op[i]*op[i+1]
            else:
                v=v*op[i+1]
        else:
            if i ==0:
                v=int(str(op[i])+str(op[i+1]))
            else:
                v=int(str(v)+str(op[i+1]))
        if v>val:
            return None
        #print(v)
    return v


            
def permute(lis, num1, num2):
    if num1==0 and num2==0:
        return [lis]
    elif num1==len(lis):
        return [[1 for x in lis]]
    elif num2 ==len(lis):
        return [[2 for x in lis]]
    
    l1 = [1 for x in range(num1)]
    l2 = [2 for x in range(num2)]
    
    l=l1+l2+ [0 for x in range(len(lis)-num1-num2)]
    
    return [list(p) for p in set(itertools.permutations(l))]


def check_val(val, op):
    v=0
    add =[0 for x in range(len(op)-1)]
    perm=[]
    for i in range(len(add)+1):
        for j in range(len(add)+1):
            perm=permute(add, i, j)
            for p in perm:
                v=add_or_mul(op, p, val)
        
                if v==val:
                    return True
    
        
    return False


for line in sys.stdin:
    val=line.split(":")
    values.append(int(val[0]))
    l =[]
    for i in val[1].split(' '):
        if not i == '':
            l.append(int(i))
    operands.append(l)
    


sum=0
for i in range(len(values)):
    if check_val(values[i], operands[i]):
        #print(values[i])
        sum+=values[i]


    
   

print(sum)
