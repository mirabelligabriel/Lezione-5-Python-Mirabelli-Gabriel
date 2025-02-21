password_corretta = "PincoPallino2022"
password = input("inserire password:")
if password == password_corretta:
    print("password corretta!")
else:
    password = input("Password errata, riprova: ")
    if password == password_corretta:
        print("Password corretta!")
    else:
        print("Password errata, tentativi terminati!")