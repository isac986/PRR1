class bankkonto:
    def __init__(self, kontonummer, saldo):
        self.kontonummer = kontonummer
        self.saldo = saldo
    
    def instättning(self, mängd):
        self.saldo += mängd
    
    def uttag(self, amount):
        self.saldo -= amount
        
    def visa_saldo(self):
        print(self.saldo)
    

info = bankkonto(12345678, 10000) 

info.instättning(500)
info.uttag(200)
info.visa_saldo()