
arr =  [1,2,3,4,5]
ei = len(arr) - 1

for i in range(len(arr)//2):
    temp = arr[i]
    arr[i] = arr[ei]
    arr[ei] = temp
    ei -= 1

print(arr)