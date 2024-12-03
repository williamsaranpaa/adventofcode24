import sys
import numpy as np
#### första delen
# left=[]
# right=[]
# for line in sys.stdin:
#     val=line.split(" ")
#     left.append(val[0])
#     right.append(val[-1])

# left.sort()
# right.sort()
# # print(left)
# # print(right)
# sum=0
# for i in range(len(left)):
#     sum+=np.abs(int(left[i])-int(right[i]))
#     #print(int(left[i])-int(right[i]))

# print(sum)

### andra delen
left=[]
right={}
for line in sys.stdin:
    val=line.split(" ")
    left.append(int(val[0]))
    if int(val[-1]) in right:
        right[int(val[-1])]+=1
    else:
        right[int(val[-1])]=1
    



# print(left)
# print(right)
sum=0
for i in left:
    if i in right:
        sum+= i*right[i]
    
    #print(int(left[i])-int(right[i]))

print(sum)