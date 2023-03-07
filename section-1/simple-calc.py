
def hoursMinSecs(seconds):
    hours = seconds // 3600 # Number of seconds in an hour (integer division)
    secs_still_remaining = seconds % 3600 # Determines the seconds left out of hours (modulo)
    minutes = secs_still_remaining // 60 # Out of the seconds; determines mins
    seconds_finally_remaining = secs_still_remaining % 60 # Seconds left
    print("Hours=" + str(hours) + " Mins=" + str(minutes) + " Seconds=" + str(seconds_finally_remaining))

# Code updated to have better named variables
print(hoursMinSecs(3905))