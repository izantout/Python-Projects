print('how many inputs do you want to have?')
days = float(input())
total_hours = total_minutes = total_seconds = 0
while days % 1 != 0:
    print('Invalid entry. Please try again')
    days = float(input())
else:
    for i in range(int(days)):
        hours = int(input('How many hours did you want to add for that day'))
        total_hours = hours + total_hours
        minutes = int(input("Hou many minutes did you want to add for that day"))
        total_minutes = minutes + total_minutes
        seconds = int(input("Hou many seconds did you want to add for that day"))
        total_seconds = seconds + total_seconds


while total_seconds >= 60:
    total_minutes = total_minutes + 1
    total_seconds = total_seconds - 60

while total_minutes >= 60:
    total_hours = total_hours + 1
    total_minutes = total_minutes - 60

hours_in_minutes = total_hours * 60
hours_in_seconds = total_hours * 3600
minutes_in_seconds = total_minutes * 60

final_minutes = total_minutes + hours_in_minutes
final_seconds = total_seconds + hours_in_seconds + minutes_in_seconds

print('In total, there are', total_hours, 'hours', total_minutes, 'minutes and ', total_seconds, 'seconds.')
print('Another way of showing this is ', final_minutes, 'minutes and', total_seconds, 'seconds', 'or', final_seconds,
      'seconds')
