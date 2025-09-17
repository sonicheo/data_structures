
def reverse_integer(num):
    new_num = 0
    while(num !=  0):
        new_num = (new_num * 10) + (num % 10)
        num = num // 10
    return new_num





if __name__ == '__main__':
    num = 1234567
    print(reverse_integer(num))