
arr =  [1,2,3,4,5]
i1 = 0
i2 = len(arr) - 1

while(i1 < i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]
    i1 += 1
    i2 -= 1

print(arr)