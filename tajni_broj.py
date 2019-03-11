tajni_broj = 7
pogodi = int(input ("Pogodi tajni broj. Izaberi broj između 1 i 10: "))


if pogodi == tajni_broj:
    print("Bravo! Pogodio si! Broj "+str(tajni_broj)+" je tajni broj.")
elif pogodi < 1:
    print("Rekao sam između 1 i 10!")
elif pogodi > 10:
    print ("Rekao sam između 1 i 10!")
else:
    print ("Žao mi je. Nisi pogodio.")