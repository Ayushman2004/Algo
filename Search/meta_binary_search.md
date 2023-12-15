# Meta Binary Search(One-sided Binary Search):

## Pre-requisite:
### Bit-wise operations(Bit manipulation):

* **Setting a Bit to _1_:**

```python
number = number | (1 << bit_position)
```

* **Setting a Bit to _0_:**
```python
number = number & ~(1 << bit_position)
```

Meta Binary Search is an algorithm similar to the general binary search, but instead of declaring the index at once, it constructs it by editing its binary one bit at a time.

### Algorithm:
1. Find the number of bits required to store the length of the array(data structure) be _n_.
1. Declare a variable with value _0_
1. Reverse iterate using the _number of bits as range_
    1. If **_key==arr[n]: return x_**
    1. Create a new variable **_new_x_** from **_x_** with the bit at position **_n_** set to **_1_**.
    1. If **_new_x <= x_** and **_arr[new_x]<=key: x=new_x_** 
1. **_If arr[x]==key: return x <br>else: return -1_**

```python
import math

arr=[0,1,2,3,4,5,6,7,8,9]
key=4
l=len(arr)

n=int(math.log2(l-1)) + 1;

p=0

for i in range(n-1,-1,-1):
    if(arr[p]==key):
        print('intex=',p)
        break
    
    new_p= p | (1 << i)

    if (arr[new_p]<=key and new_p<l):
        p=new_p

if(arr[p]==key):
    print('index=',p)
else:
    print(-1)
```