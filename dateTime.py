
import datetime

time = datetime.datetime.now()
currentHour = time.hour

def getTimeZone():
    if currentHour > 1 and currentHour <= 9:
        timeZone = "EARLY MORNING"
    elif currentHour > 9 and currentHour <= 12:
        timeZone = "MORNING"
    elif currentHour > 12 and currentHour <= 16:
        timeZone = "AFTERNOON"
    elif currentHour > 16 and currentHour <= 18:
        timeZone = "EVENING"
    elif currentHour > 18 and currentHour <= 22:
        timeZone = "NIGHT"
    elif currentHour > 22 and currentHour <= 0:
        timeZone = "EARLY NIGHT"
    else:
        timeZone = "DAWN"

    return timeZone

def getDay():
    return datetime.date.today()
