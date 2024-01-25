import datetime
import time

not_true = True
while not_true:
    print("Set a valid time. (Ex 12:00)")
    selected_time = input(">> ")
    # convert the users input to an array that separates the value from the minute value
    alarm_time = [int(n) for n in selected_time.split(":")]
    print(alarm_time)
    # Validate both the hour and minute value
    if alarm_time[0] >= 24 or alarm_time[0] < 0:
        not_true = True
    elif alarm_time[1] >= 60 or alarm_time[1] < 0:
        not_true = True
    else:
        not_true = False

# How long to wait before the alarm goes off
seconds_hms = [3600, 60, 1]
# Convert the alarm time to seconds
alarm_seconds = sum([a*b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
now = datetime.datetime.now()
current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
seconds_until_alarm_goes_off = alarm_seconds - current_time_seconds
if seconds_until_alarm_goes_off < 0:
    seconds_until_alarm_goes_off += 86400

print("Alarm is set")
print(f"The alarm will ring at {datetime.timedelta(seconds=seconds_until_alarm_goes_off)}")

# Ring the alarm
time.sleep(seconds_until_alarm_goes_off)
# Display the wake up message
print("Ring Ring... Time to wake up")

# Add countdown before the alarm rings
for i in range(0, seconds_until_alarm_goes_off):
    time.sleep(1)
    seconds_until_alarm_goes_off -= 1
    print(f"{datetime.timedelta(seconds=seconds_until_alarm_goes_off)}")
