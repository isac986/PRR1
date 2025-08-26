kryptering = {
    "a": "argon",
    "b": "banan",
    "c": "citron",
    "d": "dikt",
    "e": "elskåp",
    "f": "flor",
    "g": "guld",
    "h": "helium",
    "i": "is",
    "j": "järn",
    "k": "kalium",
    "l": "lego",
    "m": "magnesium",
    "n": "natrium",
    "o": "syre",
    "p": "plutonium",
    "q": "kvarts",
    "r": "radium",
    "s": "silver",
    "t": "titan",
    "u": "uran",
    "v": "väte",
    "w": "walesare",
    "x": "xylofon",
    "y": "yxa",
    "z": "zebra"
}

val = input("1. Krypter\n2. Dekryptera\n: ")

if val == "1":
    ordet = input("Skriv ord: ")
    
    for i in ordet:
        for key, value in kryptering.items():
            if key == i:
                print(value, end=" ")
                
elif val == "2":
    dekryptering = input("Skriv ord:")
    dekryptering = dekryptering.split(" ")
    
    for z in dekryptering:
        for key, value in kryptering.items():
            if value == z:
                print(key, end=" ")