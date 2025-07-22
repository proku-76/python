def insertion_sort(arr):
    """
    插入排序函数
    :param arr: 待排序的列表
    :return: 排序后的列表（原地排序，不返回新列表）
    """
    # 从第二个元素开始遍历（索引1到len(arr)-1）
    for i in range(1, len(arr)):
        key = arr[i]  # 当前需要插入的元素
        j = i - 1  # 从当前元素的前一个位置开始比较

        # 将比key大的元素向后移动，直到找到key的正确位置
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 元素后移
            j -= 1  # 向左移动指针

        # 将key插入到正确位置
        arr[j + 1] = key

    return arr  # 返回排序后的列表（原地修改）


# 测试示例
if __name__ == "__main__":
    test_arr = [5, 2, 4, 6, 1, 3]
    print("原始数组:", test_arr)
    sorted_arr = insertion_sort(test_arr)
    print("排序结果:", sorted_arr)