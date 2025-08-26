import random

def ssp():
    random_num = random.randint(1,3)

    if random_num == 1:
        return ("sten")
    elif random_num == 2:
        return ("sax")
    elif random_num == 3:
        return ("påse")
        
def vinnarn(hand_1, hand_2):
    if hand_1 == "sten":
        if hand_2 == "sax":
            return("sten vann!")
    if hand_1 == "sten":
        if hand_2 == "påse":
            return("påse vann!")
            
    if hand_1 == "sax":
        if hand_2 == "sten":
            return("sten vann!")
    if hand_1 == "sax":
        if hand_2 == "påse":
            return("sax vann!")
            
    if hand_1 == "påse":
        if hand_2 == "sten":
            return("påse vann!")
    if hand_1 == "påse":
        if hand_2 == "sax":
            return("sax vann!")
    if hand_1 == hand_2:
        return ("Lika!")