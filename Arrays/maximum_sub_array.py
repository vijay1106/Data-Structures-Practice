def maximum_sub_array_brute_force(nums_list) -> int:
    max_sum = sum(nums_list)
    max_sub_array = nums_list
    for i in range(0, len(nums_list) - 1):
        sub_array_sum = nums_list[i]
        if sub_array_sum > max_sum:
            max_sub_array = [nums_list[i]]
            max_sum = sub_array_sum
        else:
            for j in range(i + 1, len(nums_list) - 1):
                sub_array_sum = sub_array_sum + nums_list[j]
                if sub_array_sum > max_sum:
                    max_sub_array = nums_list[i:j + 1]
                    max_sum = sub_array_sum
                # print(" i, j ", i, j)
                # print(" considered nums_list ", nums_list[i:j+1])
                # print(" sub_array_sum ", sub_array_sum)
    print("max_sub_array ", max_sub_array)
    print("max_sum ", max_sum)


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1]
nums = [5, 4, -1, 7, 8]
maximum_sub_array_brute_force(nums)
