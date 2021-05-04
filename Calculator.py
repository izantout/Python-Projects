#Ask user what type of calculation they want done

#Output at the start of the program
def menu(): 
    print(" A - Add two Roman Numerals",'\n S - Subtract two Roman Numerals','\n M - Multiply two Roman Numerals \n D - Divide two Roman Numerals \n Q - Quit \n \nSelect A, S, M, D or Q only.', end=" ")

def add(roman1, roman2): 
    num1 = romanToArabic(roman1)
    num2 = romanToArabic(roman2)
    #add 2 roman numbers
    return arabicToRoman(num1+num2)

def sub(roman1, roman2): 
    num1 = romanToArabic(roman1)
    num2 = romanToArabic(roman2)
    #num1 should be bigger so the subtraction isn't negative
    if (num1>num2):
        #Subtact the 2 roman numbers
        return arabicToRoman(num1-num2)
    else:
        print("First number cannot be smaller than the second, that will result in a negative number")

def mul(roman1, roman2): 
    num1 = romanToArabic(roman1)
    num2 = romanToArabic(roman2)
    #Multiply the 2 roman numbers
    return arabicToRoman(num1*num2)

def div(roman1, roman2): 
    div = []
    num1 = romanToArabic(roman1)
    num2 = romanToArabic(roman2)
    if (num1>num2):
        #This returns the division of the 2 numbers
        division = arabicToRoman(int(num1/num2))
        #This returns the remainder of the 2 numbers
        remainder = arabicToRoman(int(num1%num2))
        #adds this value 
        div.append(division)
        #adds this value 
        div.append(remainder) 
        return div
    else:
        print("First number cannot be smaller than the second number since there is no 0 in the Roman letters")

#Check if the input is valid for calculation
#If not valid keep asking until we get a valid input
#If valid ask for first number
def main(): #The main code that calls other functions
    print("Welcome to the Roman Numerals Calculator\nPlease select from the following:")
    while(True):
        print()
        menu()
        Pick = input()

        #Checking for addition
        if Pick.upper()=="A":    #.upper serves to uppercase the letter inputed 
            print("Enter First Roman Number (no spaces): ")
            roman1 = getRomanN()
            print("Value of ", roman1, ": ", romanToArabic(roman1))
            print("Enter Second Roman Number (no spaces): ")
            roman2 = getRomanN()
            print("Value of ", roman2, ": ", romanToArabic(roman2))

            print(roman1, " + ", roman2, " = ", add(roman1, roman2))
            print(romanToArabic(roman1), " + ", romanToArabic(roman2), " = ", (romanToArabic(roman1) + romanToArabic(roman2)))
            continue

        #Checking for subtraction
        elif Pick.upper()=="S":   
            print("Enter First Roman Number (no spaces): ")
            roman1 = getRomanN()
            print("Value of ", roman1, ": ", romanToArabic(roman1))
            print("Enter Second Roman Number (no spaces): ")
            roman2 = getRomanN()
            print("Value of ", roman2, ": ", romanToArabic(roman2))

            print(roman1, " - ", roman2, " = ", sub(roman1, roman2))
            print(romanToArabic(roman1), " - ", romanToArabic(roman2), " = ", (romanToArabic(roman1) - romanToArabic(roman2)))
            continue

        #Checking for multiplication
        elif Pick.upper()=="M":   
            print("Enter First Roman Number (no spaces): ")
            roman1 = getRomanN()
            print("Value of ", roman1, ": ", romanToArabic(roman1))
            print("Enter Second Roman Number (no spaces): ")
            roman2 = getRomanN()
            print("Value of ", roman2, ": ", romanToArabic(roman2))

            print(roman1, " * ", roman2, " = ", mul(roman1, roman2))
            print(romanToArabic(roman1), " * ", romanToArabic(roman2), " = ", (romanToArabic(roman1) * romanToArabic(roman2)))
            continue

        #Checking for division
        elif Pick.upper()=="D":  
            print("Enter First Roman Number (no spaces): ")
            roman1 = getRomanN()
            print("Value of ", roman1, ": ", romanToArabic(roman1))
            print("Enter Second Roman Number (no spaces): ")
            roman2 = getRomanN()
            print("Value of ", roman2, ": ", romanToArabic(roman2))

            res = div(roman1, roman2)
            print("Division result and Remainder: ")
            print(roman1,  "/", roman2, " = ", res[0])
            print(roman1,  "%", roman2, " = ", res[1])
            print(romanToArabic(roman1), "/", romanToArabic(roman2), " = ", int((romanToArabic(roman1)/romanToArabic(roman2))))
            print(romanToArabic(roman1), "%", romanToArabic(roman2), " = ", int((romanToArabic(roman1)%romanToArabic(roman2))))
            continue

        #Checking for Quit
        elif Pick.upper()=="Q":   
            return print("Thank you....Goodbye")

        else:
            print("Invalid Entry, Please try again.")
#Check if the input is valid

#Function that checks if the input is valid or not
#Instead of writing 2 checking statements for each letter, .upper changes the input into an uppercase letter anc ompares it to the letter in the code directly. Saves time

#if not valid say its not valid until we get a valid input
def isValidRoman(roman): 
    for i in range(len(roman)):    
        #Checks if the letter is one of the Roman number letters
        #[i] basically checks the roman letter with the index i that is choosed. i=1 means the second letter from the left. roman[i] checks each letter to see if this letter i=the number is valid or not. The .upper is to compare oly the uppercase version of the letetr whether its inputed lowercase or upper case
        if roman[i].upper()!='I' and roman[i].upper()!='V' and roman[i].upper()!='X' and roman[i].upper()!='L' and roman[i].upper()!='C' and roman[i].upper()!='D' and roman[i].upper()!='M':
            return False   
    return True


#if its valid get Arabic equivalent, output it, and ask for second number

#check if second number is valid

#if its not valid keep asking until you get a valid number

#if its valid get Arabic equivalent, output it and Start the calculations specified in the beginning of the code

#Output the calculation specified and output the Roman number resutled after the addition of those 2 numbers.

def value(r):   
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000

#Function that changes the Roman number into its Arabic equivalent
def romanToArabic(roman): 
    i=0    
    result=0

    while(i<len(roman)):
        #Get the value of the i's roman letter.
        v1 = value(roman[i])     
        if (i+1)<len(roman):
            #get the value of the i+1's input, the one next to the roman letter.
            v2 = value(roman[i+1]) 
            #Comparing both because in roman if the letter i is smaller than the letter i+1 we need to subtract the two
            if v1>=v2:  
                #If i is bigger than i+1
                result = result + v1    
                i+= 1
            else:
                #If i is smaller than i+1
                result = result + v2-v1 
                i+= 2            
        else:
            result+= v1
            i+= 2
    return result

#Function that will tell the user that the wrong input is invalid
def getRomanN(): 
    romanNumber = input().upper()
    while(not isValidRoman(romanNumber)):
        print("Please enter a valid roman number")
        romanNumber = input()
    return romanNumber




#Output the calculation specified and output the Arabic number resulted after 
#Function that checks the Arabci number and switches it to roman
def arabicToRoman(arabic): 
    #Change each number to its roman equivalent
    number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbol = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    t = 12
    roman=""
    if arabic==0: 
        #No 0 in roman numerals
        return "There is no 0 in Roman numbers."
    while arabic:
        division = arabic//number[t]  
        arabic %= number[t]  
        while division:
            roman = roman + symbol[t]
            division-=1
        t-=1
    return roman 


#Starting the program with the main function and its inside functions
main() 
