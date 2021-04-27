def Pivot_Point(list_a, first, last):
    pivot = list_a[first]
    left = first+1
    right = left
    while True:
        while left <= right and list_a[left] <= pivot:
            left += 1
        while left <= right and list_a[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list_a[left], list_a[right] = list_a[right], list_a[left]
    list_a[first], list[right] = list_a[right], list_a[first]
    return right


def Quick_sort(list_a, first, last):
    if first < last:
        p = Pivot_Point(list_a, first, last)
        Quick_sort(list_a, first, p-1)
        Quick_sort(list_a, p+1, last)


# main
list_a = [56, 26, 93, 17, 31, 44]
n = len(list_a)
Quick_sort(list_a, 0, n-1)
print(list_a)
