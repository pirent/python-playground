import time

currentTime = int(time.time())
secondsPerHour = 60 * 60
secondsPerMinute = 60
secondsPerDay = secondsPerHour * 24

print('epoch time is {:d}'.format(currentTime))
hours = currentTime // secondsPerHour
remainder = currentTime % secondsPerHour
minutes = remainder // secondsPerMinute
second = remainder % secondsPerMinute
daysSinceEpoch = currentTime // secondsPerDay

print('Hours is {:d}'.format(hours))
print('Minutes is {:d}'.format(minutes))
print('Seconds is {:d}'.format(second))
print('Number of days since the epoch {:d}'.format(daysSinceEpoch))
