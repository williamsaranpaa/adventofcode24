import sys
import numpy as np
#### första delen

def increasing(rep):
    inc=0
    dec=0
    prev=rep[0]
    for i in range(1, len(rep)):
        if prev<rep[i]:
            inc+=1
        else:
            dec+=1
        prev=rep[i]
    #print(inc, dec)
    if inc>=dec:
        return True
    return False

def checkOK(rep, ok_recurse, inc, unsafed):
    ok=True
    increase=inc
    firstCheck=True
    unsafe=unsafed
    prev=-1
    idx=0
    
    ##första värdet fuckar med en

    for value in rep:
        val = int(value)
        if prev==-1:
            prev= int(val)
            
        elif firstCheck:
            firstCheck =False        
        
        if not prev==-1 and not firstCheck:
            if prev==val:
                if  ok_recurse and (checkOK(rep[:idx]+rep[idx+1:], False, inc, unsafe) or checkOK(rep[:idx-1]+rep[idx:], False, inc, unsafe)):
                    unsafe+=1 
                    #print(val)  
                else:
                    ok=False
                    break
            elif np.abs(prev-val)>3:
                
                if  ok_recurse and (checkOK(rep[:idx]+rep[idx+1:], False, inc, unsafe) or checkOK(rep[:idx-1]+rep[idx:], False, inc, unsafe)):
                    unsafe+=1 
                    #print(val)  
                else:
                    ok=False
                    break
            elif increase and prev>val:
                #print('here')
                if  ok_recurse and (checkOK(rep[:idx]+rep[idx+1:], False, inc, unsafe) or checkOK(rep[:idx-1]+rep[idx:], False, inc, unsafe)):
                    unsafe+=1 
                    #print(val)  
                else:
                    ok=False
                    break 
                
            elif not increase and prev<val:
                if  ok_recurse and (checkOK(rep[:idx]+rep[idx+1:], False, inc, unsafe) or checkOK(rep[:idx-1]+rep[idx:], False, inc, unsafe)):
                    unsafe+=1 
                    #print(val)  
                else:
                    ok=False
                    break
                    
        prev= int(val)
        idx+=1
    # print(rep)
    # print(unsafe)
    # print(ok)
    if ok and unsafe<2:
        return True
    else:
        return False


reports = []

for line in sys.stdin:
    val=line.split(" ")
    reports.append(val)

sum=0
for rep in reports:
    ##print(rep)
    inc=increasing(rep)
    #print(rep)
    # print(inc)
    # print(checkOK(rep, True, inc, 0))
    # print(checkOK(rep[1:], True, inc, 0))
    
    # print('__________')
    if checkOK(rep, True, inc, 0) or checkOK(rep[1:], True, inc, 0):
        #print(rep)
        sum+=1
    

#print("==============")
print(sum)

