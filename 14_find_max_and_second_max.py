
arr = [95,44,33,51,64,72,85]

def mm(arr):
    max = arr[0]
    s_max = arr[0]
    min = arr[0]
    s_min = arr[0]

    for i in arr:
        if i > max:
            max = i
        elif  max < i > s_max:
            s_max = i

        elif i < min:
            min = i
        elif min != s_min > i < s_min:
            s_min = i
    return '1,2 max:', max, s_max, '1,2 min:', min, s_min

print mm(arr)


def Range(list1):
    largest = list1[0]
    largest2 = list1[0]
    lowest = list1[0]
    lowest2 = list1[0]
    for item in list1:
        if item > largest:
            largest = item
        elif largest2 != largest2 < item:
            largest2 = item

        elif item < lowest:
            lowest = item
        elif lowest2 != lowest2 > item:
            lowest2 = item

    print("Largest element is:", largest)
    print("Smallest element is:", lowest)
    print("Second Largest element is:", largest2)
    print("Second Smallest element is:", lowest2)

list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
# list1 = [95,44,33,51,64,72,85]
Range(list1)

