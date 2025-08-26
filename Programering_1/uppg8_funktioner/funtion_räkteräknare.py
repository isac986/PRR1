startvärde = int(input("Skriv in start kapital: "))
ränta = float(input("Mata in ränta procenten i decimaltal: "))
tid = int(input("Hur många år vill du spara: "))


def ränteberäknng(startvärde, ränta, tid):
    pengar = startvärde * ((ränta+1)**tid)
    return pengar

print(ränteberäknng(startvärde, ränta, tid))