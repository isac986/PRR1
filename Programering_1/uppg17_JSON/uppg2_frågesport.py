import random

frågor = {
    "Vad kan en fågel göra?" : "flyga", #1
    "Vad heter programerings läraren?" : "emil", #2
    "Vad är huvudstaden i Sverige?" : "stockholm", #3
    "Vilket djur säger mjau": "katt", #4
    "Vilken frukt är gul och lång" : "bannan", #5
    "Vad heter havssköldpaddan i Hitta Nemo?" : "crush" #6
}

poäng = 0

while True: 

    lista = []
    for key in frågor:
        lista.append(key)

    fråga = (random.choice(lista))
    svar = input(f"{fråga}\nSvar: ")
    
    if svar == frågor[fråga]:
        poäng += 1
        print(f"Rätt!\nDu har {poäng}")
    
    else:
        poäng -= 1
        print(f"Fel!\nDu har {poäng}")
        
    if poäng == 3:
        print("Du har vunnit 3 poäng!!")
        break