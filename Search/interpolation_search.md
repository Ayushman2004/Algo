# Interpolation Search
The Interpolation Search is an improvement over the Binary Search, where the values in a sorted arrya(data structure) are uniformly distributed.

### Condition:
* Array should be sorted
* The values should be uniformly distributed

### Algorithm:
1. Label the first and last array elements as **_low_** and **_high_**
1. Calculated the position to be compared by **_pos=low + (key - arr[low]) *(high - low)/(arr[high] - arr[low])_**
1. Iterate the above using a while loop or recursion

```python
arr=[3,6,9,12,15,18,21,24,27,30]
n=len(arr)
key=21

low,high=0,n-1

while low<=high and key>=arr[low] and key<=arr[high]:
    pos = low + (key - arr[low]) *(high - low)/(arr[high] - arr[low])

    if key==arr[int(pos)]:
        print('index=',pos)
        break
    if key<arr[int(pos)]:
        high=pos-1
    if key>arr[int(pos)]:
        low=low+1
#not found statement not present
```

