def contains_duplicate(nums):
    return len(nums) != len(set(nums))

#                    сюда писать циферки
#                            ↓
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
print(contains_duplicate([1,2,3,1]))