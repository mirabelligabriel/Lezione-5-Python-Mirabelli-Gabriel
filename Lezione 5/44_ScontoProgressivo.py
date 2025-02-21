numero_articoli = int(input("Inserisci il numero di articoli acquistati: "))
prezzo_unitario = float(input("Inserisci il prezzo di ciascun articolo: "))
totale = numero_articoli * prezzo_unitario
if numero_articoli < 10:
    if prezzo_unitario >= 10:
        sconto = 0.05  
    else:
        sconto = 0.02  
elif numero_articoli == 10:
    sconto = 0.10  
else:
    if prezzo_unitario > 100:
        sconto = 0.50  
    elif prezzo_unitario < 100:
        sconto = 0.30  
    else:
        sconto = 0.35 
importo_scontato = totale * (1 - sconto)
print("L'importo finale da pagare è:", importo_scontato)