# Binary search:

Binary search is an **_interval search_** using **_divide-n-conquer_** approach in which we search the key by repeatedly dividing the data structure(array) i.e. sorted, in half and figuring out the half in which the key is most likely to be present as the data structure is sorted.

### Conditions for Binary search:
* The data structure(array) must be sorted
* Any element of the data should be accessible at any time

### Binary search algorithm:
1. Label the two extremes of the data set as high and low
1. Calculate the middle element using the previously defined high and low elements
1. Compare the value of middle element to the key
    * If key = mid_element: **_return(mid_element)_**
    * If key > mid_element: **_low=mid_element+1_**
    * If key < mid_element: **_high=mid_element-1_**
1. Iterate the cycle until **_key=mid_element_** or **_low>high_**

**The repeatition could be done iteratively(_while loop_) or recursively.**

### Using Iteration:

```python
arr=[0,1,2,3,4,5,6,7,8,9]
key=8

low=arr[0]
high=arr[-1]


while low<=high:
    mid=low + (high - low) // 2

    if arr[mid]==key:
        print('Index=',mid)
        break
    if arr[mid]>key:
        high=mid-1
        continue
    if arr[mid]<key:
        low=mid+1
        continue
```
### Using Recursion:
```python
arr=[0,1,2,3,4,5,6,7,8,9]
key=7
low,high=arr[0],arr[-1]

def binary_search(arr,low,high,key):

    mid= low + (high - low) // 2
    
    if low<high:
        if arr[mid]==key:
            return mid
        if arr[mid]>key:
            return binary_search(arr,low,mid-1,key)
        if arr[mid]<key:
            return binary_search(arr,low+1,high,key)
    else:
        return -1

print('Index=',binary_search(arr,low,high,key))
```
