# Variablen definieren
umrechnungsfaktorMeter_Feet = 3.28084

# while-Schleife
eingabeJaNein = 1
while eingabeJaNein == 1:

# Umrechnung von Meter in Feet
    wahl = input("Welcher Wert steht dir zur verfügung? Meter oder Feet?: ")
    if wahl == "Meter":
        inputMeter = float(input("Gib den Wert in Meter an: "))
        outputFeet = inputMeter * umrechnungsfaktorMeter_Feet
        print(inputMeter,"Meter sind",outputFeet,"Feet")
        
# Umrechnung von Feet in Meter
    elif wahl == "Feet":
        inputFeet = float(input("Gib den Wert in Feet an: "))
        outputMeter = inputFeet / umrechnungsfaktorMeter_Feet
        print(inputFeet,"Feet sind",outputMeter,"Meter")

# Sprung zum Anfang (while-Schleife)
    neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ")
    if neueEingabe == "Ja":
        eingabeJaNein = 1
    elif neueEingabe == "Nein":
        eingabeJaNein = 0