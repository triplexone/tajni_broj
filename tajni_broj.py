tajni_broj = 7
ime=input("Kako se zoveš? ")
pogodi = int(input ("Pogodi tajni broj. Izaberi broj između 1 i 10: "))


if pogodi == tajni_broj:
    print("Bravo "+ime+"! Čestitam! Broj "+str(tajni_broj)+" je tajni broj.")
elif pogodi < 1:
    print (ime+"! Rekao sam između 1 i 10!")
elif pogodi > 10:
    print (ime+"! Rekao sam između 1 i 10!")
else:
    print ("Žao mi je "+ime+". Više sreće drugi put.")