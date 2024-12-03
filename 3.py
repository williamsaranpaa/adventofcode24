import sys
import numpy as np
import re
#### första delen


reports = ''

for line in sys.stdin:
    reports+=line

valids = []

#print(reports) #13090869 last ans
start=0
end=0
do=True
while True:
    if do:
        
        firstnot=re.search("don't\(\)", reports[start:])
        #print(reports[start:])
        #print(len(reports))
        
        #print(firstnot)
        if firstnot==None:
            end=len(reports)
        else:
            end=start+firstnot.start()
        # print(start, end)
        # print(reports[start:end])
        # print('______')
        valids = valids + re.findall("mul\([0-9]+,[0-9]+\)", reports[start:end])
        #print(valids)
        if firstnot==None:
            break
        else:
            start+=firstnot.end()
            
        
        do=False
    else:
        #print("______________")
        #print(start)
        #print(reports[start:])
        firstok=re.search("do\(\)", reports[start:])
        #print(firstok)

        if firstnot==None:
            break
        
        start+=firstok.end()
        do=True

    

    #"[mul\([0-9]+,[0-9]+\).*]+.*don't\(\)|do\(\).*[mul\([0-9]+,[0-9]+\).*]+.*(don't\(\))*"


valids = valids 
sum=0
#print(valids)
for j in valids:
    nums=re.findall("[0-9]+", j)
    sum+=int(nums[0])*int(nums[1])

print(sum)



