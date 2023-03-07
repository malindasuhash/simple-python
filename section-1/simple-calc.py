
def hoursMinSecs(seconds):
    hours = seconds // 3600 # Number of seconds in an hour (integer division)
    secsLeft = seconds % 3600 # Determines the seconds left out of hours (modulo)
    mins = secsLeft // 60 # Out of the seconds; determines mins
    secsLeft = secsLeft % 60 # Seconds left
    print("Hours=" + str(hours) + " Mins=" + str(mins) + " Seconds=" + str(secsLeft))

print(hoursMinSecs(3905))