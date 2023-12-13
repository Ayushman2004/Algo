'''
In this algorithm we compare each and every array index with the key,
from one end to the other in order to find a match  
'''

arr=[1,2,3,4,5,6,7,8,9,0]
key=8
n=len(arr)

for i in range(0,n):
    if key == arr[i]:
        print("match found at",i)
        break
    else:
        continue
