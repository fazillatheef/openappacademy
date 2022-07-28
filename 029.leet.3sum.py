def threesum(nums):
    nums.sort()

    result = []
    for num1Idx in range(len(nums) - 2):

        # Skip all duplicates from left
        # num1Idx>0 ensures this check is made only from 2nd element onwards

        if num1Idx > 0 and nums[num1Idx] == nums[num1Idx - 1]:
            continue
        (num2Idx, num3Idx) = (num1Idx + 1, len(nums) - 1)

        while num2Idx < num3Idx:
            sum = nums[num1Idx] + nums[num2Idx] + nums[num3Idx]

            if sum == 0:

                # Add triplet to result

                result.append((nums[num1Idx], nums[num2Idx],
                                nums[num3Idx]))

                num3Idx -= 1

                # Skip all duplicates from right

                while num2Idx < num3Idx and nums[num3Idx] \
                    == nums[num3Idx + 1]:
                    num3Idx -= 1
            elif sum > 0:

                # Decrement num3Idx to reduce sum value

                num3Idx -= 1
            else:

                # Increment num2Idx to increase sum value

                num2Idx += 1
    return result
print(threesum([-1,0,1,-1,2]))