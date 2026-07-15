class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

solution = Solution()

# Voorbeeld
n = 43261596  # Binaire voorstelling: 00000010100101000001111010011100
result = solution.reverseBits(n)
print(result)  # Output: 964176192  (Binaire voorstelling: 00111001011110000010100101000000)