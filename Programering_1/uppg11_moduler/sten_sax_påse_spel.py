import sten_sax_påse

for i in range (3):
    spelare = input("Välj Sten, sax, påse: ")

    print(sten_sax_påse.vinnarn(sten_sax_påse.ssp(), spelare))