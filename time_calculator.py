
def add_time(start, end, day=""):
    day = day.casefold().title()

    # ****Define AM or PM******
    x = ''
    period = ["AM", "PM"]
    timeS = str(start).split(":")
    S_hour = int(timeS[0])
    P = timeS[1].split()
    S_minutes = int(P[0])
    PeriodS = P[1]

    timeE = str(end).split(":")
    E_hour = int(timeE[0])
    E_minutes = int(timeE[1])

    Res_H = S_hour + E_hour
    Res_Min = E_minutes + S_minutes
    cpt = 0

    while Res_Min > 59:
        Res_Min = Res_Min - 60
        Res_H += 1

    while Res_H > 12:

        Res_H = Res_H - 12
        if PeriodS == 'PM':
            PeriodS = 'AM,'

        else:
            PeriodS = 'PM,'

        cpt = cpt + 1
        if cpt == 1:
            x = "(next day)"
        if cpt >= 2:
            x = "(" + str(cpt/2) + " Days Later)"

    NewTime = str(Res_H).zfill(2)+":"+str(Res_Min).zfill(2)

    print(NewTime + " " + PeriodS + x, day)


add_time("6:30 PM", "205:12")

# Error case 3 & 6
