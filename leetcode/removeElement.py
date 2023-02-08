from typing import List

# ---------------------------- 1 ---------------------------


def removeElement(nums: List[int], val: int):

    result = [i for i in nums if i != val]
    return result


list = [1, 2, 3, 4, 5]
print(removeElement(list, 3))

# ---------------------------- 2 ---------------------------


def remove_items(test_list, item):

    # using filter() + __ne__ to perform the task
    res = list(filter((item).__ne__, test_list))

    return res


list2 = [1, 2, 3, 4, 5, 1]
print(remove_items(list2, 1))

# ---------------------------- 3 ---------------------------


def remove_all_items(nums, val):
    # count occurance of val in array and loop that number to delete all occurance
    count = nums.count(val)
    for i in range(count):
        nums.remove(val)

    return nums


list3 = [1, 2, 5, 2, 3, 4, 7, 2, 9]
print(remove_all_items(list3, 2))
