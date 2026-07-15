#1st Approach: Quicksort
# Time: n(logn)
# Space:

#2nd Approach: mergesort
# Time: n(logn) on average. n^2 in wc.
# Space:

#3nd Approach: Heapsort
# Time:
# Space:

#uitwerking nu Mergesort.

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j <len(left) and k <len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = left[j]
                    k += 1
                i += 1
            while j <len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) //2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) -1)


# Voorbeeld gebruik:
solution = Solution()
unsorted_nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = solution.sortArray(unsorted_nums)
print(sorted_nums)