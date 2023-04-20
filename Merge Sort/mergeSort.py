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

    # This function returns a randomly generated array
    def function_c(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count + 1):
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
    def select_input(self, input_type: str, elements_count: int,
                     seed: int) -> list:
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

    # This function is the Merge function from the Merge sort slides
    def Merge(self, A, left, mid, right):
        # n1
        n1 = mid - left + 1
        # n2
        n2 = right - mid

        # L array
        L = [0] * (n1)
        # R array
        R = [0] * (n2)

        # for loop for L[i]
        for i in range(0, n1):
            L[i] = A[left + i]

        # for loop for R[j[
        for j in range(0, n2):
            R[j] = A[mid + 1 + j]

        # setting all variables back to 0
        i = 0
        j = 0

        # setting k to left
        k = left

        # 1st while
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # 2nd while
        while i < n1:
            A[k] = L[i]
            i += 1
            k += 1

        # 3rd while
        while j < n2:
            A[k] = R[j]
            j += 1
            k += 1

    # This function is the Merge sort function from the mergse sort slides
    def MergeSort(self, A, left, right):
        # if left is less than right
        if left < right:
            # set the value of mid
            mid = left + (right - left) // 2
            # Call merge sort left to mid
            self.MergeSort(A, left, mid)
            # Call merge sort mid to right
            self.MergeSort(A, mid + 1, right)
            # call Merge function
            self.Merge(A, left, mid, right)

    def pa1_mergesort(self, input_type: str, elements_count: int,
                      seed: int) -> list:
        output = []
        query_list = self.select_input(input_type, elements_count, seed)

        n = len(query_list)

        # get the start time
        st = time.process_time()

        self.MergeSort(query_list, 0, len(query_list) - 1)

        et = time.process_time()
        res = et - st

        return [query_list, res]


if __name__ == '__main__':
    input_type = sys.argv[1]
    elements_count = int(sys.argv[2])
    seed = sys.argv[3]

    obj = Solution()
    ret = obj.pa1_mergesort(input_type, elements_count, seed)
    print(ret)
