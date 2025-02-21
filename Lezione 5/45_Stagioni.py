giorno = int(input("Inserisci il numero del giorno: "))
mese = int(input("Inserisci il numero del mese: "))
if mese == 1 or mese == 2 or (mese == 3 and giorno <= 20):  
    stagione = "Inverno"
elif mese == 3 or mese == 4 or mese == 5:  
    stagione = "Primavera"
elif mese == 6 or (mese == 5 and giorno <= 20):  
    stagione = "Estate"
else:
    stagione = "Data non valida per la prima metà dell'anno"
print("La stagione è:", stagione)