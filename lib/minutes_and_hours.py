def minutes_to_hour_and_minutes(minutes):
    hours = 0
    while minutes - 60 > 0:
        minutes = minutes - 60
        hours = hours + 1
    return str(hours) + ":" + str(minutes)

minutes_to_hour_and_minutes(0)