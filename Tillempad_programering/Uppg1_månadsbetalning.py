import os

def calculate_monthly_payment(principal, anual_rate, years):
    rate = anual_rate / 100 / 12
    months = years * 12

    payment = (principal * rate) / (1 - (1 + rate) ** -months)
    return payment

os.system("cls")

principal = float(input("lånebelopp: "))
anual_rate = float(input("Årsränta(%): "))
years = int(input("löptid(år): "))

payment = calculate_monthly_payment(principal, anual_rate, years)

print(f"Din betalning varje månad är: {payment: 2f} kr")

# formel a = (p*r) / (1 - 1+r) ^ -n