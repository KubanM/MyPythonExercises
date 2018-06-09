# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[j] > arr[i]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr


arr = [55, 44, 33, 12, 1]
# print bubble_sort(arr)

s = []
for i in range(len(arr)):
    for j in range(i):
        if arr[j] > arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
print arr

