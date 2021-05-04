print("Hello, I see you want to know what time it will be when the set alarm will go off")
print("To do that, you need to answer some questions.")
print("Firstly, I need to know what time is it right now, please specify")
print("Note, this input should be in the 24-hour form where for example 11 am is 11 and 11pm is 23...Midnight is 0.")
p=float(input("Current time is: "))
print("The time is",p)
#Here we know what time it is
print("Now I need to know how much time will you wait for your alarm?")
n=float(input("The number of hours you will wait is: "))
print("Your alarm will go off in",n,"hours")
#here we know how much time left for the alarm to go off
#t=the time
#n=number of hours the person needs to wait
#t is the two inputs added up
t=p+n
#a is the answer
a = t % 24
print("your alarm will ring at",a)
