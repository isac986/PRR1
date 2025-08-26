gissa_tal = 0
gissningar = 0
rätt_tal = 10

while gissningar <3:
    gissningar += 1
    gissa_tal = int(input ("Gissa ett tal mellan 0-20"))
    
    if gissa_tal == rätt_tal:
     print ("WOW du hade rätt!")
    elif gissa_tal <rätt_tal:
     print ("Gissa ett högre tal")
    else:
     print ("Gissa ett lägre tal")
