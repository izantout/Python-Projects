import sys


# Heapify code from the lecture slides but changed for smallest number
def heapify(arr, n, i):
    smallest = i                                       # Initial value of smallest is i
    l = 2 * i + 1                                      # l = Left(i)
    r = 2 * i + 2                                      # r = Right(i)
    if l < n and arr[l] < arr[smallest]:               # if l <= heap_size(A) && A[l] > A[i]
        smallest = l                                   # largest = l else largest would still be equal to i
    if r < n and arr[r] < arr[smallest]:               # if r <= heap_size(A) && A[r] > A[i]
        smallest = r                                   # smallest = r
    if smallest != i:                                  # if(largest != i)
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap(A, i, smallest)
        heapify(arr, n, smallest)                      # Heapify(A, n, smallest)

def build_heap(arr):
    n = len(arr)                                       # heap_size(A) = length(A)
    for i in range(n // 2 - 1, -1, -1):                # for(i=floor(length[a]/2) down to 1)
        heapify(arr, n, i)                             # Heapify(A, i)


def find_kth_smallest(arr, k):
    build_heap(arr)                                    # Build the heap using the inputted array

    for i in range(k):                                 # Extract the minimum element k times
        arr[0], arr[-1 - i] = arr[-1 - i], arr[0]      # Swap elements
        heapify(arr, len(arr) - i - 1, 0)              # Recall Heapify function with updated parameters

    if len(arr) < k:                                   # If k is larger than the number of elements in the heap

        return None                                    # return None

    return arr[0]                                      # else return the kth smallest element


class Solution:
    def pa2(self, arr: list[int], k: int) -> int:
        retval = find_kth_smallest(arr, k - 1)
        return retval


if __name__ == '__main__':
    arr = []
    arrtemp = sys.argv[1].split(",")
    for item in arrtemp:
        arr.append(int(item))

    k = int(sys.argv[2])
    obj = Solution()
    ret = obj.pa2(arr, k)
    print(ret)
