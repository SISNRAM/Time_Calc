
def add_time(start, end, day=""):
    day = day.casefold().title()

    # ****Define AM or PM******

    period = ["AM", "PM"]
    timeS = str(start).split(":")
    S_hour = int(timeS[0])
    P = timeS[1].split()
    S_minutes = int(P[0])
    PeriodS = P[1]
    print(PeriodS)

    timeE = str(end).split(":")
    E_hour = int(timeE[0])
    E_minutes = int(timeE[1])

    Res_H = S_hour + E_hour
    Res_Min = E_minutes + S_minutes

    while Res_H > 12:
        Res_H = Res_H - 12

    while Res_Min > 59:
        Res_Min = Res_Min - 60
        Res_H += 1

    NewTime = str(Res_H).zfill(2)+":"+str(Res_Min).zfill(2)

    print(NewTime + + ",", day)


add_time("11:06 PM", "24:59", "moNday")
