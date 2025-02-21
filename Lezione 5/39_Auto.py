prezzo = float(input("Inserisci il prezzo dell'automobile: ")) 
if 10000 <= prezzo <= 20000:
    prezzo *= 0.95 
contanti = input("Vuoi pagare in contanti? Rispondi sì o no: ")  
if contanti == "sì":
    prezzo -= 200
print("Devi pagare", prezzo)