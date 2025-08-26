ålder = int(input ("Hur gammal är du?"))
längd = float(input ("Hur lång är du i meter"))
vikt = int(input ("Hur mycket väger du i kg"))
bmi = vikt / (längd * längd)
print(f"Din bmi är {(bmi)}")

if bmi < 18.5:
    print("Du är underviktig.")
elif 18.5 <= bmi < 24.9:
    print("Du har en normal vikt.")
elif 25 <= bmi < 29.9:
    print("Du är överviktig.")
else:
    print("Du är fet.")