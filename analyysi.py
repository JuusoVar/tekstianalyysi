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


# 3 osa
sanat = teksti.split()
print(f"Tekstissä on {len(sanat)} sanaa.")

# 4 osa
sanamaarat = {}

for sana in sanat:
    if sana in sanamaarat:
        sanamaarat[sana] += 1
    else:
        sanamaarat[sana] = 1

jarjestetyt_sanat = sorted(sanamaarat, key=sanamaarat.get, reverse=True)

print(
    f"Yleisimmät sanat ovat {jarjestetyt_sanat[0]}, "
    f"{jarjestetyt_sanat[1]}, "
    f"{jarjestetyt_sanat[2]}, "
    f"{jarjestetyt_sanat[3]} ja "
    f"{jarjestetyt_sanat[4]}."
)
