import operator

def calc( *nums, op):

    result = nums[0]

    for num in nums[1:]:
        result = op(result, num)

    return result

print(calc(1, 1, 4, op = operator.add))
print(calc(1, 1, 4, op = operator.mul))
