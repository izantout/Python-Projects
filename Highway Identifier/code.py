number=int(input("Please enter a US Interstate Highway route number: \n"))
tYpe='string'
direction='string'
parent=1
first=0
while (1<=number<=999 and 1<=parent<=99) or (number<=1 or number >=1000):
  if number <=-1 or number >=1000:
    number=int(input("Please enter a US Interstate Highway route number: \n"))
  elif number>0 and number <=99:
    if number % 2 == 0:
      direction = 'east-west.'
    else:
      direction = 'north-south.'
    if number % 5 == 0:
      tYpe = 'a long-distance arterial highway'
    else:
      tYpe = ''
    print("Interstate",number,"is",tYpe,"oriented",direction,"\n")
    number=int(input("Please enter a US Interstate Highway route number: \n"))
  elif 100 <= number <= 999:
    first = number // 100
    parent = number % 100
    if parent == 0:
      continue
    elif first % 2 == 0:
      tYpe = 'loop'
    else:
      tYpe = 'spur'
    print('Interstate',number,'is a',tYpe,'highway of interstate',parent,'.','\n')
    number=int(input("Please enter a US Interstate Highway route number: \n"))
