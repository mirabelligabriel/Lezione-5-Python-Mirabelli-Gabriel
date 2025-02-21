print("Scegli un numero:")
numero1 = int(input())
if numero1 %3==0 and numero1 %5==0:
    print("Il numero è divisibile sia per 3 che per 5")
elif numero1 %3==0:
    print("Il numero è divisibile per 3 ma non per 5")
elif numero1 %5==0:
    print("Il numero è divisibile per 5 ma non per 3")