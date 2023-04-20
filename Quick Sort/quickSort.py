import sys
import random
import time

class Solution:

    # This function returns a descending sorted array.
    def function_a(self, elements_count: int) -> list:
        output = []
        for i in range(elements_count,0, -1):
            output.append(i)
        return output

    # This function returns an ascending sorted array.
    def function_b(self, elements_count: int) -> list:
        output = []
        for i in range(1, elements_count):
            output.append(i)
        return output

    # This function returns a randomly generated array
    def function_c(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count+1):
            output.append(random.randint(1, 1000000))

        return output

    # This function returns a randomly generated array
    def function_d(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count + 1):
            output.append(random.randint(1, 2000000))

        return output

    # This function selects a correct action based on the input a, b or c.
    def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        if input_type == "a":
            output = self.function_a(elements_count)
        if input_type == "b":
            output = self.function_b(elements_count)
        if input_type == "c":
            output = self.function_c(elements_count, seed)
        if input_type == "d":
            output = self.function_d(elements_count, seed)
        return output

    # This function is the Partition function from the QuickSort slides
    def Partition(self, A, p, r):
        # Set the variable x to be A[r]
        x = A[r]
        # Set i to be p - 1
        i = p - 1
        # For loop
        for j in range(p, r):
            # If A[j] is less than or equal to x
            if A[j] <= x:
                # Increment i
                i = i + 1
                # Exchange A[i] with A[j]
                A[i], A[j] = A[j], A[i]
        # Exchange A[i + 1] with A[r]
        A[i + 1], A[r] = A[r], A[i + 1]
        # Return i + 1
        return i + 1

    # This function is the QuickSort function from the quickSort slides
    def QuickSort(self, A, p, r):
        # Check if p is less than r
        if p < r:
            # Call the Partition function and save it to q
            q = self.Partition(A, p, r)
            # Recursive call Quicksort function for p & q - 1
            self.QuickSort(A, p, q - 1)
            # Recursive call Quicksort function for q + 1 & r
            self.QuickSort(A, q + 1, r)

    def pa1_Quicksort(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        query_list = self.select_input(input_type, elements_count, seed)

        n = len(query_list)

        # get the start time
        st = time.process_time()

        # your quicksort algorithm comes here ...
        self.QuickSort(query_list, 0, len(query_list) - 1)

        et = time.process_time()
        res = et - st

        return [query_list, res]

if __name__ == '__main__':
    # the input type is either a, b or c
    # corresponding to function_a, function_b and function_c.
    input_type = sys.argv[1]

    elements_count = int(sys.argv[2])

    # input seed as 2, so we have the same randomly
    # generated array.
    # you can change it for your testing.
    seed = int(sys.argv[3])

    obj = Solution()
    # the return value is an array of array.
    ret = obj.pa1_Quicksort(input_type, elements_count, seed)
    print(ret)
