# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
  i = 0
  j = 0

  len1 = len(arrA)
  len2= len(arrB)

  arr = []

  while (i < len1) and (j < len2):
    if (arrA[i] < arrB[j]):
        arr.append(arrA[i])
        i+=1
    else:
        arr.append(arrB[j])
        j+= 1

    if i == len1:
        arr.extend(arrB[j:])
    else:
        arr.extend(arrA[i:])
    return arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
       return arr
    l = len(arr) // 2 
    arrA = merge_sort(arr[:l])
    arrB = merge_sort(arr[l:])
    arr = merge(arrA, arrB)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

