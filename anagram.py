
def turn_list(word):
    new_arr = []
    for i in word:
        new_arr.append(i)
    return new_arr

def sort_arr(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j], arr[i]
    
    return arr

def anagram(str1,str2):
    if len(str1) != len(str2):
        return False

    str1_arr = sort_arr(turn_list(str1))
    str2_arr = sort_arr(turn_list(str2))

    for i in range(len(str1_arr)):
        if str1_arr[i] != str2_arr[i]:
            return False

    return True

if __name__ == '__main__':
    str1 = "restful"
    str2 = "fluster"
    print(anagram(str1,str2))