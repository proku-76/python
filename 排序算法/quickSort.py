def quick_sort(arr):
    """
    快速排序主函数
    """
    # 递归终止条件：数组长度小于等于1时直接返回
    if len(arr) <= 1:
        return arr

    # 选择基准值（pivot）
    pivot = arr[len(arr) // 2]  # 通常选择中间元素作为基准值

    # 分区操作
    left = [x for x in arr if x < pivot]  # 小于基准值的元素
    middle = [x for x in arr if x == pivot]  # 等于基准值的元素
    right = [x for x in arr if x > pivot]  # 大于基准值的元素

    # 递归排序左右分区并合并结果
    return quick_sort(left) + middle + quick_sort(right)


# 测试示例
if __name__ == "__main__":
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    print("原始数组:", test_arr)
    sorted_arr = quick_sort(test_arr)
    print("排序结果:", sorted_arr)

    # 更多测试用例
    test_cases = [
        [],
        [5],
        [9, 3],
        [1, 6, 3, 2, 4, 5],
        [10, 7, 8, 9, 1, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ]

    for i, case in enumerate(test_cases):
        print(f"\n测试用例 {i + 1}: {case}")
        result = quick_sort(case)
        print(f"排序结果: {result}")