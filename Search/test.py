import math
arr=[0,1,2,3,4,5,6,7,8,9]
n=len(arr)
key=8

step=math.sqrt(n)

while arr[int(step)]< key:
    p_step = step
    step = step + math.sqrt(n)

while arr[int(p_step)]<key:
    p_step=p_step+1 

    if arr[int(p_step)]==min(step,n):
        print('not_found')
        break

if arr[int(p_step)]==key:
    print('index=',int(p_step))