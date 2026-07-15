#1st Approach: Hashset (CHAT GPT)
# Time: O(n)
# Space:


def findDisappearedNumbers(nums):
    result = set(range(1, len(nums) + 1))

    for num in nums:
        if num in result:
            result.remove(num)

    return list(result)

# Voorbeeldgebruik
input_array = [4, 3, 2, 7, 8, 2, 1]
output = findDisappearedNumbers(input_array)
print(output)