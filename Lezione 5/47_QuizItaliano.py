print("Ciao! Facciamo un quiz.")
risposta1 = int(input("In che anno è nato Alessandro Manzoni? "))
if risposta1 > 1785:
    print("Uhm… è nato prima dell’anno", risposta1)
    risposta2 = input("Vuoi studiare di più? Rispondi sì o no ")
    if risposta2== "sì":
        print("Ottimo.")
    else:
        print("Ti conviene farlo ugualmente.")
elif risposta1 < 1785 :
    print("Uhm… è nato dopo dell’anno", risposta1)
else:
    print("Bene. Hai inserito l’anno corretto.")
    print("Adesso potrai proseguire con l'interrograzione.")
    print()
    print("Chi sono i due protagonisti dei Promessi Sposi?")
    personaggio1 = input("Primo protagonista: ")
    personaggio2 = input("Secondo protagonista: ")
    if personaggio1 == "Renzo" and personaggio2 == "Lucia":
        print("Bravo! Hai indovinato.")
    elif personaggio1 == "Renzo" and personaggio2 != "Lucia":
        print("Hai indovinato solo un nome, Renzo. Hai sbagliato Lucia.")
    elif personaggio1 != "Renzo" and personaggio2 == "Lucia":
        print("Hai indovinato solo un nome, Lucia. Hai sbagliato Renzo.")
    else:
        print("Mi dispiace, ma non hai indovinato. Sono Renzo e Lucia.")
print("A presto.")