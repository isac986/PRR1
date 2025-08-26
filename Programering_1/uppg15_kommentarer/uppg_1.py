#kollar om tal är perfekt tal
def är_perfekt_tal(tal):
    summa = 0
    #loopar igenom 1 till tal
    for i in range(1, tal):
        #kollar om tal är jämnt delbart med i
        if tal % i == 0:
            summa += i
    #retunerar sant om summa och tal är lika
    return summa == tal