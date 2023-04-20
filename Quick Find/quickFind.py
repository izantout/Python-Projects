import sys


# Partition function from the slides
def partition(A, p, r):
    x = A[r]  # x = A[r]
    i = p - 1  # i = p - 1
    for j in range(p, r):  # for j=p to r-1
        if A[j] <= x:  # if A[j[ <= x
            i += 1  # i = i + 1
            A[i], A[j] = A[j], A[i]  # exchange A[i] with A[j]
    A[i + 1], A[r] = A[r], A[i + 1]  # exchange A[i+1] with A[r]
    return i + 1  # return i+1


# kth smallest algorithm from the requirements PDF
def kthSmallest(arr, l, r, k):
    if 0 < k <= r - l + 1:
        q = partition(arr, l, r)                  # make the partition using the last element
        if q - l == k - 1:                        # if position is same as k
            return arr[q]
        elif q - l > k - 1:                       # if position is more, # recur for left subray
            return kthSmallest(arr, l, q - 1, k)

        else:                                     # else recur for right subarray
            return kthSmallest(arr, q + 1, r, k - q + l - 1)
    return None                                   # if k is out of range, return None


class Solution:
    def pa2(self, arr: list[int], k: int) -> int:
        retval = kthSmallest(arr, arr[0], arr[-1], k - 1)
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
