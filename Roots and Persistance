# while true:
while True:
# input 1 
  answ3r = int(input("Please enter an integer (negative integer to quit): "))
# num=input 1 to have another copy of it when changed.
  num = answ3r
  print("For the integer: ",answ3r)
# if input <=9 and >=0:
  if answ3r <= 9 and answ3r>= 0:
# print the number as is.
    add_persistance = 1
    add_root = answ3r
    mul_persistance = 1
    mul_root = answ3r
# elif number <0:
  elif answ3r < 0:
# stop program and output stop message.
    print("Thanks for playing with numbers...Goodbye")
    break
# else:
  else:
# add_persistance = 0
    add_persistance = 0
# mul_persistance = 0
    mul_persistance = 0
# while number > 9
    while answ3r > 9:
# multiple persistance + =1
      mul_persistance += 1
# multiple root = 1
      mul_root = 1
# while input > 9
      while answ3r > 0:
# newnum = input % 10
        newnum = answ3r % 10
# mulroot = mulroot * newnum
        mul_root = mul_root * newnum
# input = input // 10
        answ3r = answ3r // 10
# input = mulroot
      answ3r = mul_root
# while num > 9
    while num > 9:
# add_persistance += 1
      add_persistance += 1
# addroot = 0
      add_root = 0
# while num > 0
      while num > 0:
# split = num % 10
        split = num % 10
# addroot = addroot + split
        add_root = add_root + split
# num = num // 10
        num = num // 10
# num = addroot
      num = add_root
  print("Additive Persistance: ",add_persistance,"\n","Additive Root: ",add_root)
  print("Multiplicative Persistance: ",mul_persistance,"\n","Multiplicative Root: ",mul_root)
print("Proccess finished with exit code 0")
