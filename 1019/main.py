__author__ = 'darkwolf'


time = int(input())
hours = minutes = int(0)
while time >= 3600:
    hours += 1
    time -= 3600
while time >= 60:
    minutes += 1
    time -= 60
seconds = time
print("%i:%i:%i" % (hours, minutes, seconds))

