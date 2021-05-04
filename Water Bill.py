#assign a variable with y as value
#while loop the following if y is true
#while loop to repeat each input if the input is invalid
#input 1 is costumer code for all cases add or with upper case letter.
#input 2 is beginning meter reading
#input 3 is end meter reading
#if end>beginning:
#end-beginning
#if end<beginning
  #do 1 with 9 zeros hadda - beginning... value plus end... display as gallons knowing that its 10th of a gallon awal chi 3al yamin
  #divide number by 10. use '{:.1f}.format(value) to have 1 digit after virgule
#if input 1:
  #$5.00 plus $0.0005 per gallon used
  #calculate cost
#if input 2
  #$1000.00 for 4 million gallons or less, and $0.00025 for each additional gallon used
    #calculate cost
#if input 3
  # $1000.00 if usage does not exceed 4 million gallons;
  # $2000.00 if usage exceeds 4 million gallons but does not exceed 10 million gallons; and
  # $2000.00 plus $0.00025 for each additional gallon if usage exceeds 10 million gallons.
    #calculate cost
#else:
  #print cost 0 and gallons useed 0 "{:0>9}".format(end)
#TO USE DOLLAR SIGN USE THE FOLLOWING: print("Your tax liability is",'${:,.2f}'.format(14382 + ((x - 84200) * 0.24)))
#end-beginning to find addech saraf
#print inputs 
#print cost
#print gallons consumed.
#ask if they want to repeat the code
#y yes n no others invalid






run_again = 'y' 
#while #CODE IS NOT C OR I OR R input
while run_again == 'y' or run_again == 'Y':
  CODE = input("Enter the customer's code: ")
  while CODE != 'c' and CODE != 'C' and CODE != 'I' and CODE != "i" and CODE != 'R' and CODE != 'r':
    print("Invalid Code")
    CODE = input("Enter costomor's code ")
  else:
    BEGINNING = int(input("Enter the customer's beginning meter reading: "))
    while BEGINNING > 999_999_999:
      print("Invalid Entry")
      BEGINNING = int(input("Enter the customer's beginning meter reading: "))
    else:
      END = int(input("Enter the customer's ending meter reading: "))
      while END < 0 and END > 999_999_999:
        print("Inavlid Entry")
        END = int(input("Enter the customer's ending meter reading: "))
      else:
          if END >= BEGINNING:
            TOTAL_GALLONS = (END - BEGINNING)/10
          else:
            TOTAL_GALLONS = ((1_000_000_000 - BEGINNING) + END)/10
          if BEGINNING<= 999_999_999 and END<= 999_999_999 and BEGINNING >=   0 and END >= 0:
            if CODE == 'r' or CODE == 'R':
              COST = 5 + (0.0005 * TOTAL_GALLONS)
            elif CODE == 'c' or CODE == 'C':
              if TOTAL_GALLONS <= 4_000_000:
                COST = 1_000
              else:
                COST = 1_000 + ((TOTAL_GALLONS - 4_000_000) * 0.00025)
            elif CODE == 'i' or CODE == 'I':
              if TOTAL_GALLONS < 4_000_000:
                COST = 1_000
              elif TOTAL_GALLONS > 4_000_000 and TOTAL_GALLONS < 10_000_000:
                COST = 2_000
              else:
                COST = 2_000+((TOTAL_GALLONS - 10_000_000) * 0.00025)
          else:
            print("Invalid Entry")
            COST = 0
            TOTAL_GALLONS = 0
  print("Customer code:",CODE)
  print("Beginning meter reading:","{:0>9}".format(BEGINNING))
  print("Ending meter reading:","{:0>9}".format(END))
  print("Gallons of water used:",'{:.1f}'.format(TOTAL_GALLONS))
  print("Amount billed:",'${:.2f}'.format(COST))
  run_again = input("Would you like to try again? Y for yes and N for no")
  while run_again!='n' and run_again != 'N' and run_again!='y' and run_again!='Y':
    run_again = input("Enter a correct input ")
print("Goodbye")
