print("Benvenuto nella calcolatrice!")
print("Scegli un numero:")
numero1 = float(input())
print("Scegli un secondo numero:")
numero2 = float(input())
print("Scegli l'operatore: +, -, *, /")
operatore = input()
if operatore == "+":
    print("Il risultato dell'addizione è:", numero1 + numero2)
elif operatore == "-":
    print("Il risultato della sottrazione è:", numero1 - numero2)
elif operatore == "*":
    print("Il risultato della moltiplicazione è:", numero1 * numero2)
elif operatore == "/":
    if numero2 != 0:
        print("Il risultato della divisione è:", numero1 / numero2)