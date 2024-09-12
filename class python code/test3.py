def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# 示例使用
if __name__ == '__main__':
    import random
    arr = [random.randint(0, 100) for _ in range(20)]
    print("原始数组:", arr)
    sorted_arr = quicksort(arr)
    print("排序后的数组:", sorted_arr)
