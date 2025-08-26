import datetime

år = datetime.date.today().strftime("%Y%m%d")

namn = input ("Vad heter du? ")
födelse_datum = int(input ("ÅÅÅÅMMDD: "))

ålder = int((int(år) - int(födelse_datum)) / 10000)

print (f"Hej {namn} du är {ålder} år gammal.")