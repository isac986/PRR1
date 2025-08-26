class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def introduktion(self):
        print(f"Mitt namn är {self.namn} och jag är {self.ålder} år gammal.")

class Elev(Person):
    def __init__(self, namn, ålder, student_id):
        super().__init__(namn, ålder)
        self.student_id = student_id

    def lär_sig(self):
        print("Lär mig nu!")

    def introduktion(self):
        print(f"Hej, jag är {self.namn}, en elev med ID {self.student_id}, och jag är {self.ålder} år gammal.")

class Lärare(Person):
    def __init__(self, namn, ålder, anställd_id):
        super().__init__(namn, ålder)
        self.anställd_id = anställd_id

    def lär(self):
        print("Lär ut nu!")

    def introduktion(self):
        print(f"Hej, jag är {self.namn}, en lärare med ID {self.anställd_id}, och jag är {self.ålder} år gammal.")

t1 = Lärare("Mio", 40, "T123456789")
e1 = Elev("Isac", 17, "E123456789")
e2 = Elev("Olle", 17, "E987654321")

skolans_personer = [t1, e1, e2]

for person in skolans_personer:
    person.introduktion()