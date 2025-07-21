def merge_sort(arr):
    # 递归终止条件：数组长度小于等于1时直接返回
    if len(arr) <= 1:
        return arr

    # 1. 分解：将数组平分成左右两部分
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # 2. 递归排序左右子数组
    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    # 3. 合并排序后的子数组
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    i = j = 0

    # 比较两个子数组的元素并按序合并
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 添加左数组剩余元素
    while i < len(left):
        merged.append(left[i])
        i += 1

    # 添加右数组剩余元素
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# 测试示例
if __name__ == "__main__":
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    print("原始数组:", test_arr)
    sorted_arr = merge_sort(test_arr)
    print("排序结果:", sorted_arr)