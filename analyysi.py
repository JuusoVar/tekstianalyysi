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

# osa 5
merkkimaarat = {}
for merkki in teksti:
    if not merkki.isspace():
        if merkki in merkkimaarat:
            merkkimaarat[merkki] += 1
        else:
            merkkimaarat[merkki] = 1

jarjestetyt_merkit = sorted(merkkimaarat, key=merkkimaarat.get, reverse=True)

print(
    f"Yleisimmät merkit ovat {jarjestetyt_merkit[0]}, "
    f"{jarjestetyt_merkit[1]}, "
    f"{jarjestetyt_merkit[2]}, "
    f"{jarjestetyt_merkit[3]} ja "
    f"{jarjestetyt_merkit[4]}."
)

# bonus
suomi = ["on", "ja", "ei", "että", "oli", "myös", "kun", "sekä", "niin", "mutta"]
ruotsi = ["är", "det", "som", "inte", "var", "på", "ett", "men"]
englanti = ["and", "but", "the", "of", "it", "in", "was", "that", "but"]

suomi_maara = 0
ruotsi_maara = 0
englanti_maara = 0

for sana in sanat:
    sana = sana.lower()
    if sana in suomi:
        suomi_maara += 1
    if sana in ruotsi:
        ruotsi_maara += 1
    if sana in englanti:
        englanti_maara += 1

if suomi_maara > ruotsi_maara and suomi_maara > englanti_maara:
    print("Teksti on todennäköisesti suomea.")
elif ruotsi_maara > suomi_maara and ruotsi_maara > englanti_maara:
    print("Teksti on todennäköisesti ruotsia.")
elif englanti_maara > suomi_maara and englanti_maara > ruotsi_maara:
    print("Teksti on todennäköisesti englantia.")