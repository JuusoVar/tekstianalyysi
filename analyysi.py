# 1 kohta
while True:
    tiedostonimi = input("Anna tekstitiedoston nimi: ")

    try:
        with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
            teksti = tiedosto.read()
        break
    except FileNotFoundError:
        print("Tiedostoa ei löydy")

# 2 osa
print(f"Tekstissä on {len(teksti)} merkkiä.")
