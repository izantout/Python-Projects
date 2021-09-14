input_number = float(input('How many inputs do you want to have? '))
total_hours = total_minutes = total_seconds = 0
while input_number % 1 != 0:
    input_number = float(input('Invalid entry. Please try again'))
else:
    for i in range(int(input_number)):
        print('Day', i + 1)
        hours = int(input('How many hours did you want to add for this day '))
        total_hours = hours + total_hours
        minutes = int(input("How many minutes did you want to add for this day "))
        total_minutes = minutes + total_minutes
        seconds = int(input("How many seconds did you want to add for this day "))
        total_seconds = seconds + total_seconds

while total_seconds >= 60:
    total_minutes += 1
    total_seconds -= 60

while total_minutes >= 60:
    total_hours += 1
    total_minutes -= 60

hours_in_minutes = total_hours * 60
hours_in_seconds = total_hours * 3600
minutes_in_seconds = total_minutes * 60

final_minutes = total_minutes + hours_in_minutes
final_seconds = total_seconds + hours_in_seconds + minutes_in_seconds

print('In total, there are', total_hours, 'hours', total_minutes, 'minutes and', total_seconds, 'seconds.')
print('Another way of showing this is ', final_minutes, 'minutes and', total_seconds, 'seconds', 'or', final_seconds,
      'seconds')

print(' Hours                            Minutes                            Seconds')
print('  ',total_hours,'                               ',total_minutes,'                                ',total_seconds)
