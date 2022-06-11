
def add_time(start, end, day=""):
    day = str(day).casefold().title()

    # ****Define AM or PM******
    x = ''
    Days = [" Monday", " Tuesday", " Wednesday",
            " Thursday", " Friday", " Saturday", " Sunday"]
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

    # ****** days later *****
    if (Res_H / 24).is_integer():
        tmp = Res_H / 24
    else:
        tmp = int(Res_H / 24) + 1

    dayIndice = 0
    while Res_H > 12:
        Res_H = Res_H - 12
        dayIndice += 1
        if PeriodS == 'PM':
            PeriodS = 'AM'
        else:
            PeriodS = 'PM'

        # ****Time Later***** error with same days

        if tmp == 1:
            x = " (next day)"
        if tmp >= 2:
            x = " (" + str(tmp) + " Days Later)"

    if Res_H == 12 and PeriodS == 'AM':
        PeriodS = 'PM'
    elif Res_H == 12 and PeriodS == 'PM':
        PeriodS = 'AM'

    NewTime = str(Res_H) + ":"+str(Res_Min).zfill(2)
    # **** Adding Comma****
    if len(day) != 0:
        day = ", " + day

    print(NewTime + " " + PeriodS, end="")

    DaysLater = E_hour % 7
    if day != "":
        if dayIndice >= 2:
            print("," + Days[DaysLater], end='')

        elif dayIndice == 1 and P[1] == "AM":
            print(day, end="")
    # if dayIndice >= 2:
    print(x, end='')


add_time("3:30 PM", "2:12")
