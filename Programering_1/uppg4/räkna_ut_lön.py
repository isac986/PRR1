lön = 0.01
dagar = 0

räknesätt = int(input ("Lön efter dagar (1) eller hur många dagar (2) "))

if räknesätt == 1:
    dagar = int(input ("Hur många dagar vill du räkna ut?"))
    for i in range (1,dagar+1):
        lön *=2
    print (f"Du kommer tjärna {lön} efter att ha jobbat {dagar}")
    
elif räknesätt == 2:
    mål = int(input("Hur mycket pengar vill du tjärna "))
    while lön < mål:
        lön*=2
        dagar+=1
    print (f"Efter {dagar} dagar har du tjärnat {lön}")