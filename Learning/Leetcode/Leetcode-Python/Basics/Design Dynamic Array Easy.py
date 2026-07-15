#Dynamic array = resizable array = ArrayList in Java = Vector in C++
# Follow-up

class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

# O(1)
    def insert(self, i: int, n: int) -> None:
        self.arr[i] = n

# O(1) - Avg case / Ammortized
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size]
        self.size +=1

    def popback(self) -> int:
        self.size -=1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


# Voorbeeld van gebruik:
dynamic_array = DynamicArray(5)

print("Size:", dynamic_array.getSize())  # Output: 0
print("Capacity:", dynamic_array.getCapacity())  # Output: 5

dynamic_array.pushback(10)
dynamic_array.pushback(20)
dynamic_array.pushback(30)

print("Size:", dynamic_array.getSize())  # Output: 3
print("Capacity:", dynamic_array.getCapacity())  # Output: 5

print("Element at index 1:", dynamic_array.get(1))  # Output: 20

dynamic_array.popback()

print("Size after pop:", dynamic_array.getSize())  # Output: 2