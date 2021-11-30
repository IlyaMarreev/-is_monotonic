nums = []

print("Введите длину массива")
a = int(input())
def is_monotonic(nums):
    nums_4 = []
    nums_5 = []
    nums_6 = []
    for count in range(a):
        spisok = int(input())
        nums.append(spisok)
        nums_4.append(spisok)
        nums_5.append(spisok)
        nums_6.append(spisok)
    nums_2 = nums
    nums_2.sort()
    nums_3 = nums_4
    nums_3.sort(reverse = True)

    if nums_5 == nums_2:
        print("True")
        return(True)
    elif nums_6 == nums_4:
        print("True")
        return(True)
    else:
        print("False")
        return(False)
is_monotonic(nums)
