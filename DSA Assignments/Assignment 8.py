#Question - 1
#Time complexity:
#best case = O(n)
#worst case = T(n) = T(n-1) + n => O(n^2)
def partition(arr,p,q):
    pivot = arr[p]
    i = p
    for j in range(i+1,q+1):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i+1

def SelectionProcedure(arr,p,q,k):
    if p == q:
        return arr[p]
    elif p < q:
        position = partition(arr,p,q)
        if position == k:
            return arr[position-1]
        elif k < position:
            SelectionProcedure(arr,p,position-1,k)
        else:
            SelectionProcedure(arr,position+1,q,k)

#driver code
arr = [40, 30, 26, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = SelectionProcedure(arr,0,len(arr)-1,k)
print(f"The Kth largest element of the array is {result}")

#Question - 2
#In place modification algorithm - QuickSort.
#space complexity - Constant.
#Best case - array divides into half - O(nlogn)
#Worst case - o(n^2)
def partition(Nums,p,q):
    pivot = Nums[p]
    i = p
    for j in range(i+1,q+1):
        if Nums[j] <= pivot:
            i+=1 #update the position of i
            Nums[i],Nums[j] = Nums[j],Nums[i]
    Nums[i],Nums[p] = Nums[p],Nums[i] #Final swap of ith element and the pivot element.
    return i

def SortColors(Nums,p,q):
    if p == q: #Small problem
        return Nums[p]
    elif p < q:
        mid = partition(Nums,p,q)
        SortColors(Nums,p,mid-1)
        SortColors(Nums,mid+1,q)
    return Nums #Inplace modification

#driver code:
Nums = [2,0,2,1,1,0]
result = SortColors(Nums,0,len(Nums)-1)
print(f"The Sorted colors : {result}")

#Question - 3
#Time complexity:
#best case = O(n)
#worst case = T(n) = T(n-1) + n => O(n^2)
def partition(arr,p,q):
    pivot = arr[p]
    i = p
    for j in range(i+1,q+1):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i+1

def SelectionProcedure(arr,p,q,k):
    if p < q:
        position = partition(arr,p,q)
        if k == position:
            return arr[position-1]
        elif k < position:
            SelectionProcedure(arr,p,position-1,k)
        else:
            SelectionProcedure(arr,position+1,q,k)

#driver code
arr = [40, 30, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = SelectionProcedure(arr,0,len(arr)-1,k)
print(f"The Kth largest element of the array is {result}")

#Question - 4
#Approach - Boyer Moore Voting algorithm
#Using Hashing approach, it takes space complexity as O(n) (Dictionary)
"""
If the majority element is present in the array, whatever be the candidate element at last,
the count will always be greater than zero, else if not present, count will be
equal to zero.
The Final check for which element is the majority element is an optional case.
"""
#Time complexity - O(n)
#space complexity  - O(1) constant
def MajorityElement(Nums):
    candidate = None
    count = 0
    i = 0
    while i < len(Nums):
        if count == 0:
            candidate = Nums[i]
            count+= 1
        else:
            if candidate == Nums[i]:
                count+=1
            count-=1
        i+=1

    c = 0
    for i in range(len(Nums)):
        if Nums[i] == candidate:
            c+=1
    if c > len(Nums)//2:
        return candidate
    return None

#driver code:
Nums = [2, 2, 1, 1, 1, 2, 2]
result = MajorityElement(Nums)
print(f"The majority element present is {result}")














