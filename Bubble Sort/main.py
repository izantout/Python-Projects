import sys


class Solution:

    def data_conversion(self, data, convert_to):
        if convert_to == "int":
            return int(data)

        if convert_to == "list":
            new_input = []
            data = data.split(",")
            for item in data:
                new_input.append(int(item))

            return new_input

        if convert_to == "bool":
            return bool(data)

    def pa0(self, s: list) -> list:
        # Big for loop going through all elements
        for i in range(0, len(s)):
            # Small for loop going from the 1st element to the element before the last element (-i) since we know that
            # that element is for sure going to be the biggest from the previous iteration
            for j in range(0, len(s) - 1 - i):
                # If the element of the right of the current element is greater than the current element
                if s[j] > s[j + 1]:
                    # Set temp to the right element
                    temp = s[j + 1]
                    # Set the right element to the bigger element
                    s[j + 1] = s[j]
                    # Set the current element to the smaller element
                    s[j] = temp
        # Return s
        return s


if __name__ == '__main__':
    # argv takes the input as a string.
    # to run pa1 we need to convert argv (or input data)
    # to the datatype that pa0 accepts.
    # data_conversion function converts an string to
    # convert_to variable suitable for pa1 program input.
    # "convert_to" variable can be one of the followings:
    # "list", "int", "bool"
    # note: a list of integers should be entered as a
    # comma separated sequence in command line as input for a program.
    # For example, myproject.py 1,2,3,4,5

    # Setting convert_to variable
    convert_to = "list"

    # Read the input string from the command line
    s = sys.argv[1]

    # Craeting an object from Solution class
    obj = Solution()

    # Call "data_conversion" method to convert s (input string )
    # to a desire input datatype that is set for convert_to
    s = obj.data_conversion(s, convert_to)

    # calling tha pa1 mnethod to run the program
    ret = obj.pa0(s)

    print(ret)
