ålder = input("Hur gammal är du: ")

try:
    ålder = int(ålder)
    assert 0 < ålder < 120, "Åldern måste vara ett positivt tal och mindre än 120."
    
    print(f"Din ålder är {ålder}.")

except ValueError:
    print("Åldern måste vara ett heltal.")

except AssertionError as e:
    print(e)
