
# Sentinel Linear Search:

Sentinel linear search is a variation of the linear search in which the last element of the array is asssigned
the key(sentinel value) and a while loop is iterated to search the position of the key.

<br>

```python

arr=[1,2,3,4,5,6,7,8,9,0]
key=7
n=len(arr)

last=arr[-1]
arr[-1]=key

index=0

while arr[index]!=key: 
    index++

arr[-1]=last

if index < n -1:
    print('Index=',index)
else:
    print('Object not found')

```

<br>

**The main advantage of sentinel linear search over a regular linear search is that it eliminates the need to check for the end of array in every iteration, as with the sentinel value assigned at the end of the array the algorithm is destined to eliminated the iteration.**


**This can result in slight performance improvement as it reduces the number of conditions checked in each iteration i.e. the end of the array**


