# importing for histogram
from __future__ import print_function, division

# IMPORTING time TO CALCULATE TOTAL TIME TAKEN IN EXECUTION
import time

# transforms file into a list
a_file = open("demo.txt", "r")
list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)
a_file.close()


# print(list_of_lists)


# function to check the list is sorted in ascending order or not.
# ===== Part A ======
def is_sorted(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return 'False'
    return 'True'


# ===== Part B ======
def is_anagram(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)
    # If length of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return 'False'
    str1 = str1.lower()
    str2 = str2.lower()
    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)
    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 'False'
    return 'True'


# ===== Part C ======
import random

NUMBER_OF_STUDENTS = 23
TRIALS = 1000


def has_duplicates(my_list):
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1


def generate_random_birthdays():
    return [random.randint(1, 365) for student in range(NUMBER_OF_STUDENTS)]


def stats(TRIALS):
    duplicate_count = 0.0
    for i in range(TRIALS):
        if has_duplicates(generate_random_birthdays()):
            duplicate_count += 1
    print(
        f"In {TRIALS} classrooms with {NUMBER_OF_STUDENTS} students, {(float(duplicate_count) / TRIALS) * 100:.1f} had students with duplicate birthdays.")


# ===== Part D ======
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    print("remove_duplicates (", lst, "): ", new_list)


remove_duplicates([1, 2, 2])
# ===== Part E ======
import time


def append_method():
    start = time.time()
    file = open('demo.txt', "r")
    word_list = []
    for line in file:
        line = line.split()
        for word in line:
            word_list.append(word)

    end = time.time()
    print("Total words: ", len(word_list))
    print("First 10 words: ", word_list[:10])
    print("Time elapsed: ", end - start)


# ===== Part E ======
import time


def t_method():
    start = time.time()
    file = open('demo.txt', "r")
    word_list = []
    for line in file:
        line = line.split()
        for word in line:
            word_list = word_list + [word]

    end = time.time()
    print("Total words: ", len(word_list))
    print("First 10 words: ", word_list[:10])
    print("Time elapsed: ", end - start)


# ===== Part F ======
def bisect(my_list, x):
    all_occurrences = []
    last_found_index = -1
    element_found = True

    while element_found:
        try:
            last_found_index = my_list.index(x, last_found_index + 1)
            all_occurrences.append(last_found_index)
        except ValueError:
            element_found = False

    if len(all_occurrences) == 0:
        print("bisect", my_list)
        print(x, "Not found")
    else:
        print("bisect", my_list)
        print(x, "found at index: ", all_occurrences)


# ===== Part G ======
import matplotlib.pyplot as plt


def letter_his(data):
    # data= input ("enter a sentence: ")# ask user for sentence
    count_dir = {}  # store letters with count
    for i in data:
        if i in count_dir.keys():
            count_dir[i] += 1  # if letter is already in dir then increase value of letter by one
        else:
            count_dir[i] = 1  # insert letter and give value one

    del count_dir[' ']  # remove spaces count from dir
    sorted_dir = {}  # to store sorted letters
    # sorting the letters and there counts
    for i in sorted(count_dir.keys()):
        sorted_dir[i] = count_dir[i]
    print(list(sorted_dir.keys()), list(sorted_dir.values()))
    # plotting the bar graph
    plt.bar(list(sorted_dir.keys()), list(sorted_dir.values()))
    plt.show()


# ===== Part H ======

words = []
f = open('demo.txt', 'r')
# makes the word in the list each on a separate line
for line in f:
    for word in line.strip().split():
        words.append(word.strip())

f.close()

# After sorting
for i in range(len(words)):
    if i == 0 or words[i - 1] != words[i]:
        sortedList = words[i]


# print("Done")These 3 lines are just for me to see where my code is at and to check that everything is working properly
# print(type(words))
# print(''.join(words))


# Checking how many words are in the file
def numberofwords():
    print(len(words))


string1 = words

str = ''.join(words)

# def count_all():
counta = countb = countc = countd = counte = countf = countg = counth = counti = countj = countk = countl = 0
countm = 0
countn = counto = countp = countq = countr = counts = countt = countu = countv = countw = countx = county = 0
countz = countsp = 0
countA = countB = countC = countD = countE = countF = countG = countH = countI = countJ = countK = countL = 0
countM = 0
countN = countO = countP = countQ = countR = countS = countT = countU = countV = countW = countX = countY = 0
countZ = 0
for i in str:
    if i == 'a':
        counta = counta + 1
    elif i == 'b':
        countb = countb + 1
    elif i == 'c':
        countc = countc + 1
    elif i == 'd':
        countd = countd + 1
    elif i == 'e':
        counte = counte + 1
    elif i == 'f':
        countf = countf + 1
    elif i == 'g':
        countg = countg + 1
    elif i == 'h':
        counth = counth + 1
    elif i == 'i':
        counti = counti + 1
    elif i == 'j':
        countj = countj + 1
    elif i == 'k':
        countk = countk + 1
    elif i == 'l':
        countl = countl + 1
    elif i == 'm':
        countm = countm + 1
    elif i == 'n':
        countn = countn + 1
    elif i == 'o':
        counto = counto + 1
    elif i == 'p':
        countp = countp + 1
    elif i == 'q':
        countq = countq + 1
    elif i == 'r':
        countr = countr + 1
    elif i == 's':
        counts = counts + 1
    elif i == 't':
        countt = countt + 1
    elif i == 'u':
        countu = countu + 1
    elif i == 'v':
        countv = countv + 1
    elif i == 'w':
        countw = countw + 1
    elif i == 'x':
        countx = countx + 1
    elif i == 'y':
        county = county + 1
    elif i == 'z':
        countz = countz + 1
    if i == 'A':
        countA = countA + 1
    elif i == 'B':
        countB = countB + 1
    elif i == 'C':
        countC = countC + 1
    elif i == 'D':
        countD = countD + 1
    elif i == 'E':
        countE = countE + 1
    elif i == 'F':
        countF = countF + 1
    elif i == 'G':
        countG = countG + 1
    elif i == 'H':
        countH = countH + 1
    elif i == 'I':
        countI = countI + 1
    elif i == 'J':
        countJ = countJ + 1
    elif i == 'K':
        countK = countK + 1
    elif i == 'L':
        countL = countL + 1
    elif i == 'M':
        countM = countM + 1
    elif i == 'N':
        countN = countN + 1
    elif i == 'O':
        countO = countO + 1
    elif i == 'P':
        countP = countP + 1
    elif i == 'Q':
        countQ = countQ + 1
    elif i == 'R':
        countR = countR + 1
    elif i == 'S':
        countS = countS + 1
    elif i == 'T':
        countT = countT + 1
    elif i == 'U':
        countU = countU + 1
    elif i == 'V':
        countV = countV + 1
    elif i == 'W':
        countW = countW + 1
    elif i == 'X':
        countX = countX + 1
    elif i == 'Y':
        countY = countY + 1
    elif i == 'Z':
        countZ = countz + 1
    else:
        countsp = countsp + 1

freq_i1 = "2. The frequency of each letter in the file: "
freq_a1 = ("[(‘A’, ", countA, "),", "(‘B’, ", countB, "),", "(‘C’, ", countC, "),", "(‘D’, ", countD, "),",
           "(‘E’, ", countE, "),", "(‘F’, ", countF, "),")
freq_a2 = ("(‘G’, ", countG, "),", "(‘H’, ", countH, "),",
           "(‘I’, ", countI, "),", "(‘J’, ", countJ, "),", "(‘K’, ", countK, "),", "(‘L’, ", countL, "),",
           "(‘M’, ", countM, "),")
freq_a3 = ("(‘N’, ", countN, "),", "(‘O’, ", countO, "),", "(‘P’, ", countP, "),",
           "(‘Q’, ", countQ, "),", "(‘R’, ", countR, "),", "(‘S’, ", countS, "),")
freq_a4 = ("(‘T’, ", countT, "),",
           "(‘U’, ", countU, "),", "(‘V’, ", countV, "),", "(‘W’, ", countW, "),", "(‘X’, ", countX, "),",
           "(‘Y’, ", countY, "),", "(‘Z’, ", countZ, ")]")
freq_a5 = ("[(‘a’, ", counta, "),", "(‘b’, ", countb, "),", "(‘c’, ", countc, "),", "(‘d’, ", countd, "),",
           "(‘e’, ", counte, "),", "(‘f’, ", countf, "),")
freq_a6 = ("(‘g’, ", countg, "),", "(‘h’, ", counth, "),",
           "(‘i’, ", counti, "),", "(‘j’, ", countj, "),", "(‘k’, ", countk, "),", "(‘l’, ", countl, "),",
           "(‘m’, ", countm, "),")
freq_a7 = ("(‘n’, ", countn, "),", "(‘o’, ", counto, "),", "(‘p’, ", countp, "),",
           "(‘q’, ", countq, "),", "(‘r’, ", countr, "),", "(‘s’, ", counts, "),")
freq_a8 = ("(‘t’, ", countt, "),",
           "(‘u’, ", countu, "),", "(‘v’, ", countv, "),", "(‘w’, ", countw, "),", "(‘x’, ", countx, "),",
           "(‘y’, ", county, "),", "(‘z’, ", countz, "),]"
           )

freq_i2 = "3. The frequency of upper case letters in the file: "
freq_u1 = ("[(‘A’, ", countA, "),", "(‘B’, ", countB, "),", "(‘C’, ", countC, "),", "(‘D’, ", countD, "),",
           "(‘E’, ", countE, "),", "(‘F’, ", countF, "),")
freq_u2 = ("(‘G’, ", countG, "),", "(‘H’, ", countH, "),",
           "(‘I’, ", countI, "),", "(‘J’, ", countJ, "),", "(‘K’, ", countK, "),", "(‘L’, ", countL, "),",
           "(‘M’, ", countM, "),")
freq_u3 = ("(‘N’, ", countN, "),", "(‘O’, ", countO, "),", "(‘P’, ", countP, "),",
           "(‘Q’, ", countQ, "),", "(‘R’, ", countR, "),", "(‘S’, ", countS, "),")
freq_u4 = ("(‘T’, ", countT, "),",
           "(‘U’, ", countU, "),", "(‘V’, ", countV, "),", "(‘W’, ", countW, "),", "(‘X’, ", countX, "),",
           "(‘Y’, ", countY, "),", "(‘Z’, ", countZ, ")]")

freq_i3 = "4. The frequency of lower case letters in the file: "
freq_l1 = ("[(‘a’, ", counta, "),", "(‘b’, ", countb, "),", "(‘c’, ", countc, "),", "(‘d’, ", countd, "),",
           "(‘e’, ", counte, "),", "(‘f’, ", countf, "),")
freq_l2 = ("(‘g’, ", countg, "),", "(‘h’, ", counth, "),",
           "(‘i’, ", counti, "),", "(‘j’, ", countj, "),", "(‘k’, ", countk, "),", "(‘l’, ", countl, "),",
           "(‘m’, ", countm, "),")
freq_l3 = ("(‘n’, ", countn, "),", "(‘o’, ", counto, "),", "(‘p’, ", countp, "),",
           "(‘q’, ", countq, "),", "(‘r’, ", countr, "),", "(‘s’, ", counts, "),")
freq_l4 = ("(‘t’, ", countt, "),",
           "(‘u’, ", countu, "),", "(‘v’, ", countv, "),", "(‘w’, ", countw, "),", "(‘x’, ", countx, "),",
           "(‘y’, ", county, "),", "(‘z’, ", countz, "),]"
           )
print("")
print("")
print("======== Part A: is_sorted ========")
print("is_sorted([1,2,2]): ", is_sorted([1, 2, 2]))
print("is_sorted([1,2,2]): ", is_sorted(['b', 'a']))
print("")

print("======== Part B: is_anagram ========")
print("is_anagram(listen,silent):", is_anagram(str1='listen', str2='silent'))
print("is_anagram(listen,silent):", is_anagram(str1='cat', str2='dog'))
print("")

print("======== Part C: The Birthday Paradox ========")
print("")
stats(TRIALS)
print("")
print("======== Part D: remove_duplicates ========")
print("")

remove_duplicates([1, 2, 2])
print("")
print("======== Part E: With append ========")
append_method()
print("")

print("======== Part E: With idiom t = t + [x] ========")
t_method()
print("")
print("The append method takes less time since it takes less time to instantiate and append a list than to add the "
      "time of each step taken ")
print("")

print("======== Part F: bisect ========")
print("")
bisect([2, 5, 8, 45, 47, 67], 45)
bisect([2, 5, 8, 45, 47, 67], 43)
print("")
print("======== Part G: Dictionary ========")
print("")
letter_his("hello how are you")

print("")
print("======== Part H: Read the Moby Deck text file ========")
print("1. Number of words in test file: ", len(words), "\n")

# 2. 3. 4.
# count_all()
# Replacing each capital letter with a lowercase letter and each lower case letter with an uppercase letter
print("5. Convert all uppercase to lower case and visa versa, write in a new file")
print("Started!")
str.swapcase()
print("Completed!")
print("")

print("6. Towards the end of the file (or in a new file) write the result of 1 - 4 in an output text file")
print("Started!")
print("Completed!")
print("")

print("7. Plot the letter frequency")
print("Good Bye")

# outputting H into a different file

final_file = open('final.txt', 'w')
'''
final_file.write("======== Part A: is_sorted ========")
final_file.write("\nis_sorted([1,2,2]): ")
final_file.write(is_sorted([1, 2, 2]))
final_file.write("\nis_sorted(['b','a']): ")
final_file.write(is_sorted(['b', 'a']))

final_file.write("\n======== Part B: is_anagram ========")
final_file.write("\nis_anagram(listen,silent):")
final_file.write(is_anagram(str1='listen', str2='silent'))
final_file.write("\nis_anagram(cat,dog):")
final_file.write(is_anagram(str1='cat', str2='dog'))

final_file.write("\n======== Part C: The Birthday Paradox ========")

final_file.write("\n======== Part D: remove_duplicates ========")

final_file.write("\n======== Part E: With append ========")
final_file.write("Number of words: ")
listOfWords = constructListUsingAppend()

final_file.write("\n======== Part E: With idiom t = t + [x] ========")

final_file.write("\n======== Part F: bisect ========")

final_file.write("\n======== Part G: Dictionary ========")
'''
final_file.write("\n======== Part H: Read the Moby Deck text file ========")
# 1.
final_file.write("\n1. Number of words in test file: ")
final_file.write('{:04d}\n'.format(len(words)))

final_file.write('\n')

# 2.
final_file.write(freq_i1 + '\n')
freq_a1 = freq_a1.__str__()
final_file.write(freq_a1 + '\n')
freq_a2 = freq_a2.__str__()
final_file.write(freq_a2 + '\n')
freq_a3 = freq_a3.__str__()
final_file.write(freq_a3 + '\n')
freq_a4 = freq_a4.__str__()
final_file.write(freq_a4 + '\n')
freq_a5 = freq_a5.__str__()
final_file.write(freq_a5 + '\n')
freq_a6 = freq_a6.__str__()
final_file.write(freq_a6 + '\n')
freq_a7 = freq_a7.__str__()
final_file.write(freq_a7 + '\n')
freq_a8 = freq_a8.__str__()
final_file.write(freq_a8 + '\n')

final_file.write('\n')

# 3.
final_file.write(freq_i2 + '\n')
freq_u1 = freq_u1.__str__()
final_file.write(freq_u1 + '\n')
freq_u2 = freq_u2.__str__()
final_file.write(freq_u2 + '\n')
freq_u3 = freq_u3.__str__()
final_file.write(freq_u3 + '\n')
freq_u4 = freq_u4.__str__()
final_file.write(freq_u4 + '\n')

final_file.write('\n')

# 4.
final_file.write(freq_i3 + '\n')
freq_l1 = freq_l1.__str__()
final_file.write(freq_l1 + '\n')
freq_l2 = freq_l2.__str__()
final_file.write(freq_l2 + '\n')
freq_l3 = freq_l3.__str__()
final_file.write(freq_l3 + '\n')
freq_l4 = freq_l4.__str__()
final_file.write(freq_l4 + '\n')

# Replacing each capital letter with a lowercase letter and each lower case letter with an uppercase letter
final_file.write("5. Convert all uppercase to lower case and visa versa, write in a new file" + '\n')
final_file.write("Started!" + '\n')
final_file.write(str.swapcase() + '\n')
final_file.write("Completed!" + '\n')

final_file.write("6. Towards the end of the file (or in a new file) write the result of 1 - 4 in an output text file"
                 + '\n')
final_file.write("Started!" + '\n')
final_file.write("Completed!" + '\n')

final_file.write("7. Plot the letter frequency" + '\n')
final_file.write("Good Bye")

final_file.close()
# Histogram for a given sentence
import pandas as pd
import matplotlib.pyplot as plt

test = "A tenth branch of the king's ordinary revenue, said to be grounded on the consideration of his guarding and " \
       "protecting the seas from pirates and robbers, is the right to royal fish, which are whale and sturgeon. And t" \
       "hese, when either thrown ashore or caught near the coast, are the property of the king."

# convert input to list of chars so it is easy to get into pandas
char_list = list(test)

# create a dataframe where each char is one row
df = pd.DataFrame({'chars': char_list})
# drop all the space characters
df = df[df.chars != ' ']
# add a column for aggregation later
df['num'] = 1
# group rows by character type, count the occurrences in each group
# and sort by occurrence
df = df.groupby('chars').sum().sort_values('num', ascending=False) / len(df)

plt.bar(df.index, df.num, width=0.5, color='g')
plt.show()

# convert input to list of chars so it is easy to get into pandas
char_list = list(str)

# create a dataframe where each char is one row
df = pd.DataFrame({'chars': char_list})
# drop all the space characters
df = df[df.chars != ' ']
# add a column for aggregation later
df['num'] = 1
# group rows by character type, count the occurrences in each group
# and sort by occurrence
df = df.groupby('chars').sum().sort_values('num', ascending=False) / len(df)

plt.bar(df.index, df.num, width=0.5, color='g')
plt.show()
