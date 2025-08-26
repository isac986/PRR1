class bok:
    def __init__(self, titel, författare, antal_sidor):
        self.titel = titel
        self.författare = författare
        self.antal_sidor = antal_sidor
    def info(self):
        print(f"titel {self.titel}, {self.författare}, {self.antal_sidor}")


bok1 = bok("1884", "George Orwell", 328)
bok2 = bok("Sagan om Ringen", "J.R.R Tolkien", 432)
bibliotek = [bok1, bok2]

for bok in bibliotek:
    bok.info()