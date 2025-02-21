print("Benvenuto nel mio programma di conversazione")
print()
risposta=input("Ti piace andare in bicicletta? Rispondi sì o no: ")
if risposta=="sì":
    print("Molto bene! Ti terrai in forma.")
    risposta2 = input("Ti piace anche il basket? ")
    if risposta2=="sì":
        print("Allora sei un atleta!")
    else:
        print("Uno sport è meglio di niente!")
else:
    print("Forse ti piace qualche altro sport.")