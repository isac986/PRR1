def dividera(a, b):
    try:
        summa = a / b
    except ZeroDivisionError:
        return "Division med noll är inte tillåten."
    else:
        return summa