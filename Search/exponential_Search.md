# Exponential Search:
### Steps:
1. Check if array index 0 is equal to key, if true **_return 0_**
1. Scan the array after every interval i, where the value of i will double after each interval, **_while arr[i]<=key & i<n_**
1. Once the interval range is found then search it using a Binary search

```python
def expo(arr,key):

    n=len(arr)
    i=0

    if arr[i]==key:
        return i
    i=1

    while arr[i]<=key and i<n:
        i=i*2

    ans=binary_search(arr,i/2,min(i,n-1),key)
    return ans


def binary_search(arr,low,high,key):

    mid= low + (high - low) // 2
    
    if low<=high:
        if arr[int(mid)]==key:
            return mid
        if arr[int(mid)]>key:
            return binary_search(arr,low,mid-1,key)
        if arr[int(mid)]<key:
            return binary_search(arr,low+1,high,key)
    else:
        return -1

arr=[4,8,12,16,20,24,28,32,36,40]
key=32
print('Index=',expo(arr,key))
```