# Jump Search:
In Jump Search we search the data set in two steps:
* Scaning the data set(array) while jumping or skipping a fixed number of steps or indexs every time **e.g. arr[m],arr[2m],arr[3m]....**
* Once we find the range such that **arr[km] < key < arr[(k+1)m]** then we search this range using a simple linear search

### Performace:
**Linear Search < Jump Search < Binary Search**

* **We calculate the jump size we take sqr.root of the length of the array(data set)**

```python
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
```