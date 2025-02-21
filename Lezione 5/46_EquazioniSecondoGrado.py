import math
print("forma dell'equazione: ax^2 + bx + c = 0")
a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))
c = float(input("Inserisci il coefficiente c: "))
if a == 0:
    print("L'equazione non è di secondo grado.")
    if b != 0:
        print("L'equazione è di primo grado.")
        x = -c / b
        print("La soluzione è x =", x)
    else:
        print("Non è un'equazione valida.")
else:
    delta = (b ** 2) - (4 * (a * c))
    print("Delta =", delta)
    if delta < 0:
        print("L'equazione non ha soluzioni reali.")
    elif delta == 0:
        x = -b / (2 * a)
        print("L'equazione ha una soluzione doppia:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("L'equazione ha due soluzioni:", round(x1, 2), "e", round(x2, 2))