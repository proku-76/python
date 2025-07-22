def quick_sort_inplace(arr, low=0, high=None):
    """
    原地分区的快速排序实现（节省空间）
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 分区操作，返回基准值位置
        pivot_index = partition(arr, low, high)

        # 递归排序左右分区
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    """
    分区函数（双指针法）
    """
    # 选择基准值（这里选择最后一个元素）
    pivot = arr[high]
    i = low  # 指向小于基准值的最后一个元素

    for j in range(low, high):
        if arr[j] < pivot:
            # 交换元素，将小于基准值的元素移到左侧
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # 将基准值放到正确位置
    arr[i], arr[high] = arr[high], arr[i]
    return i