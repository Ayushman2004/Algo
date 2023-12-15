# Ternary Search:
Ternary search is a searching algorithm quite similar to binarysearching, but unlike binary search where the data set was divided into two part in tarnery search the data set in divided into three equal parts.

* **Just like Binary search, Ternary search also requires sorted data set**
* **And also any element of the data should be accessible at any time**

**The mid_elements are decided on the basis of the following equations:**
* _mid1 = low + (high-low)/3_
* _mid2 = high - (high-low)/3_

Which divided the data set(array) into following three sections: **[low,mid1]**,**[mid1,mid2]**,**[mid2,high]**

### Iteration:
* If **_key==mid1 or mid2: return mid1 or mid2_**
* If **_key<mid1: high=mid1-1_**
* If **_key>mid2: low=mid2+1_**
* If **_mid1<key<mid1:  low=mid1+1, high=mid2-1_**

```python
arr=[0,1,2,3,4,5,6,7,8,9]
key=4

low,high=arr[0],arr[-1]

while(low<=high):

    mid1= low + (high-low)//3
    mid2= high - (high-low)//3

    if key==arr[mid1]:
        print('Index=',mid1)
        break
    if key==arr[mid2]:
        print('Index=',mid2)
        break

    if key<arr[mid1]:
        high=mid1-1
    elif key>arr[mid2]:
        low=mid2+1
    else:
        low=mid1+1
        high=mid2-1

#Not found case not included
```