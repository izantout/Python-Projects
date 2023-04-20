import sys
import random
import time


class Solution:

    # This function returns a descending sorted array.
    def function_a(self, elements_count: int) -> list:
        output = []
        for i in range(elements_count, 0, -1):
            output.append(i)
        return output

    # This function returns an ascending sorted array.
    def function_b(self, elements_count: int) -> list:
        output = []
        for i in range(1, elements_count):
            output.append(i)
        return output

    def function_c(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count + 1):
            output.append(random.randint(1, 1000000))

        return output

    def function_d(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count + 1):
            output.append(random.randint(1, 2000000))

        return output

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

    # This is the insertion sort algorithm from the slides
    def InsertionSort(self, A, n):
      for i in range(1, n):
        # key is the ith element of the array
        key = A[i]
        # j = i - 1
        j = i - 1
        # while loop
        while j >= 0 and key > A[j]:
          A[j + 1] = A[j]
          j -= 1
        # set j+1th element to key
        A[j + 1] = key

    def pa1_insertionsort(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        query_list = self.select_input(input_type, elements_count, seed)

        # get the start time
        st = time.process_time()

        self.InsertionSort(query_list, len(query_list))

        et = time.process_time()
        res = et - st

        return [query_list[::-1], res]


if __name__ == '__main__':
    input_type = sys.argv[1]
    elements_count = int(sys.argv[2])
    seed = sys.argv[3]

    obj = Solution()
    ret = obj.pa1_insertionsort(input_type, elements_count, seed)
    print(ret)
