import sys
import numpy as np
import re
#### första delen
word='MAS'

### första delen
# def look_around(box, k, l, dir):
#     k=k+dir[0]
#     l=l+dir[1]
    
#     for i in range(1, len(word)):
#         if k>=0 and l>=0 and  k<len(box) and  l<len(box[0]):
#             if box[k][l]==word[i]:
#                 k=k+dir[0]
#                 l=l+dir[1]
#             else:
#                 return 0
#         else:
#             return 0
#     return 1
    



# def search(box, k, l):
#     value=0
    
#     for i in range(-1, 2):
#         for j in range(-1, 2):
            
#             if k+i>=0 and l+j>=0 and  k+i<len(box) and  l+j<len(box[0]):
#                 # print(box[k+i][l+j])
                
#                 if box[k+i][l+j]=='M':
#                         value+=look_around(box, k, l, (i, j))
            
#     # print(value)
#     # print(k, l)
#     # print('___________')
#     return value
####andra delen

directions=[(1, 1), (1, -1), (-1, -1), (-1, 1)]
found=[]
def look_around(box, k, l, dir):
    for i in range(len(word)):
        if k>=0 and l>=0 and  k<len(box) and  l<len(box[0]):
            if box[k][l]==word[i]:
                k=k+dir[0]
                l=l+dir[1]
            else:
                return False
        else:
            return False
    return True

def search(box, k, l):
    value=0

    for d in directions:
        i=d[0]
        j=d[1]
        if k+i>=0 and l+j>=0 and  k+i<len(box) and  l+j<len(box[0]):
            if box[k+i][l+j]=='A':
                    
                    if look_around(box, k, l, (i, j)):
                        entry=(k+i, l+j)
                        if entry in found:
                            value+=1
                        else:
                            found.append(entry)
    return value

    
    
box=[]


for line in sys.stdin:
    vec=[]
    for c in line:
        if not c=='\n':
            vec.append(c)
    
    box.append(vec)
    
sum=0

for i in range(len(box)):
    for j in range(len(box[i])):
        if box[i][j]==word[0]:
            
            sum+=search(box, i, j)

#1997 too high
print(sum)



