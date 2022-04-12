# brute force approach
def two_sum_brute_force(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums) - 1):
            if nums[i] + nums[j] == target:
                print(i, j)
                break


# Here we are creating a lookup table for each of the number in the list
# Then for every number in the list we confirm if the difference to the target exists, if it does we will print.
# if not we will update it to the dict for lookup to the next value in the list
def two_sum_look_up(nums, target):
    lookup_dict = {}
    for i in range(0, len(nums) - 1):
        lookup_number = target - nums[i]
        if lookup_dict.get(lookup_number) is not None:
            print(lookup_dict.get(lookup_number), i)
            break
        else:
            lookup_dict[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
# two_sum(nums, target)
two_sum_look_up(nums, target);

